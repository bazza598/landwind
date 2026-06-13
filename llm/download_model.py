#!/usr/bin/env python3
"""Download an LLM from the Hugging Face Hub to a local directory.

This only fetches the model files (weights, tokenizer, config) so they are
cached locally and ready for offline inference. Run `chat.py` afterwards to
actually talk to the model.

Examples:
    # Download the default model into ./llm/models/
    python llm/download_model.py

    # Download a specific model
    python llm/download_model.py --model meta-llama/Llama-3.2-1B-Instruct

    # Download into a custom directory
    python llm/download_model.py --out /data/models

Gated models (e.g. Llama, Gemma) require a Hugging Face account, accepting the
model license on its page, and authenticating first:
    huggingface-cli login        # or: export HF_TOKEN=hf_xxx
"""
from __future__ import annotations

import argparse
import os
import sys

DEFAULT_MODEL = os.environ.get("HF_MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
DEFAULT_OUT = os.path.join(os.path.dirname(__file__), "models")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download a Hugging Face model locally.")
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model repo id on the Hub (default: {DEFAULT_MODEL}).",
    )
    p.add_argument(
        "--out",
        default=DEFAULT_OUT,
        help="Directory to download the model into (default: ./llm/models).",
    )
    p.add_argument(
        "--token",
        default=os.environ.get("HF_TOKEN"),
        help="Hugging Face access token for gated/private models "
        "(or set the HF_TOKEN environment variable, or run `huggingface-cli login`).",
    )
    p.add_argument(
        "--revision",
        default=None,
        help="Specific git revision/branch/tag to download (default: main).",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        sys.stderr.write(
            "Missing dependencies. Install them first:\n"
            "    pip install -r llm/requirements.txt\n"
        )
        return 1

    target = os.path.join(args.out, args.model.replace("/", "__"))
    os.makedirs(target, exist_ok=True)

    print(f"Downloading '{args.model}' -> {target}")
    if args.revision:
        print(f"  revision: {args.revision}")

    try:
        path = snapshot_download(
            repo_id=args.model,
            revision=args.revision,
            local_dir=target,
            token=args.token,
            # Skip redundant heavy formats; keep safetensors + config + tokenizer.
            ignore_patterns=["*.pth", "*.onnx", "*.msgpack", "*.h5"],
        )
    except Exception as exc:  # noqa: BLE001 - surface a friendly message
        msg = str(exc)
        sys.stderr.write(f"\nDownload failed: {exc}\n")
        if "allowlist" in msg.lower() or "egress" in msg.lower():
            sys.stderr.write(
                "\nNetwork access to huggingface.co appears to be blocked by an egress\n"
                "policy (common in sandboxed/CI environments). Run this on a machine\n"
                "with internet access, or allowlist huggingface.co.\n"
            )
        elif "gated" in msg.lower() or "401" in msg or "403" in msg:
            sys.stderr.write(
                "\nThis looks like a gated/private model. Accept its license on the\n"
                "model page and authenticate with `huggingface-cli login` or HF_TOKEN.\n"
            )
        return 1

    print(f"\nDone. Model files are in:\n    {path}")
    print("\nRun it with:")
    print(f'    python llm/chat.py --model "{path}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
