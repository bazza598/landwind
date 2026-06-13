#!/usr/bin/env python3
"""Run a local Hugging Face LLM: single prompt or interactive chat.

The model is loaded with `transformers`. If you pass a local path (from
`download_model.py`) it runs fully offline; if you pass a Hub repo id it will
download on first use and cache it.

Examples:
    # Interactive chat with the default model (downloads on first run)
    python llm/chat.py

    # One-shot prompt
    python llm/chat.py --prompt "Write a tagline for an AI automation agency."

    # Use a model you already downloaded locally
    python llm/chat.py --model ./llm/models/Qwen__Qwen2.5-0.5B-Instruct
"""
from __future__ import annotations

import argparse
import os
import sys

DEFAULT_MODEL = os.environ.get("HF_MODEL", "Qwen/Qwen2.5-0.5B-Instruct")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Chat with a local Hugging Face LLM.")
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Local path or Hub repo id (default: {DEFAULT_MODEL}).",
    )
    p.add_argument(
        "--prompt",
        default=None,
        help="Run a single prompt and exit. Omit for interactive chat.",
    )
    p.add_argument(
        "--system",
        default="You are a helpful assistant.",
        help="System prompt that sets the assistant's behavior.",
    )
    p.add_argument("--max-new-tokens", type=int, default=512)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument(
        "--device",
        default="auto",
        help="Device map: 'auto', 'cpu', or 'cuda' (default: auto).",
    )
    return p.parse_args()


def load_model(model_id: str, device: str):
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError:
        sys.stderr.write(
            "Missing dependencies. Install them first:\n"
            "    pip install -r llm/requirements.txt\n"
        )
        raise SystemExit(1)

    print(f"Loading model '{model_id}' ...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=dtype,
        device_map=device,
    )
    return tokenizer, model


def generate(tokenizer, model, messages, args) -> str:
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    output_ids = model.generate(
        **inputs,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        do_sample=args.temperature > 0,
        pad_token_id=tokenizer.eos_token_id,
    )
    # Strip the prompt tokens so we only decode the new response.
    new_tokens = output_ids[0][inputs["input_ids"].shape[-1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def main() -> int:
    args = parse_args()
    tokenizer, model = load_model(args.model, args.device)

    if args.prompt is not None:
        messages = [
            {"role": "system", "content": args.system},
            {"role": "user", "content": args.prompt},
        ]
        print("\n" + generate(tokenizer, model, messages, args))
        return 0

    print("\nInteractive chat. Type 'exit' or Ctrl-C to quit.\n")
    messages = [{"role": "system", "content": args.system}]
    try:
        while True:
            user = input("you> ").strip()
            if user.lower() in {"exit", "quit"}:
                break
            if not user:
                continue
            messages.append({"role": "user", "content": user})
            reply = generate(tokenizer, model, messages, args)
            messages.append({"role": "assistant", "content": reply})
            print(f"\nbot> {reply}\n")
    except (KeyboardInterrupt, EOFError):
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
