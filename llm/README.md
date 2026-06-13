# Local LLM (Hugging Face)

Download and run an open LLM from the [Hugging Face Hub](https://huggingface.co/models)
on your own machine. This is standalone tooling — it is **not** wired into the
Nexlify landing page, which stays a pure static site.

> Note: model weights are large (hundreds of MB to many GB) and are **not**
> committed to this repo. The `llm/models/` directory is gitignored.

## 1. Install dependencies

A Python virtual environment is recommended:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r llm/requirements.txt
```

For GPU acceleration, install the CUDA build of PyTorch that matches your
system first — see https://pytorch.org/get-started/locally/.

## 2. Download a model

```bash
# Default: Qwen/Qwen2.5-0.5B-Instruct (small, fast, CPU-friendly, Apache-2.0)
python llm/download_model.py

# Or pick any model from the Hub
python llm/download_model.py --model meta-llama/Llama-3.2-1B-Instruct
```

Files land in `llm/models/<repo-id>/`.

**Gated models** (Llama, Gemma, Mistral, …) require accepting the license on
the model page and authenticating:

```bash
huggingface-cli login        # or: export HF_TOKEN=hf_xxxxx
```

## 3. Run it

```bash
# Interactive chat
python llm/chat.py

# One-shot prompt
python llm/chat.py --prompt "Write a tagline for an AI automation agency."

# Use the copy you downloaded locally (fully offline)
python llm/chat.py --model ./llm/models/Qwen__Qwen2.5-0.5B-Instruct
```

Useful flags: `--system`, `--max-new-tokens`, `--temperature`, `--device`
(`auto` | `cpu` | `cuda`).

## Choosing a model

| Model | Size | Good for |
|---|---|---|
| `Qwen/Qwen2.5-0.5B-Instruct` (default) | ~1 GB | Laptops / CPU, quick tests |
| `Qwen/Qwen2.5-3B-Instruct` | ~6 GB | Better quality, modest GPU |
| `meta-llama/Llama-3.2-1B-Instruct` | ~2.5 GB | Gated; needs HF login |
| `microsoft/Phi-3.5-mini-instruct` | ~7 GB | Strong small model, GPU |

Both `HF_MODEL` (env var) and `--model` override the default everywhere.
