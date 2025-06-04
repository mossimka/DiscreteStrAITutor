# OpenAI Practice Lab

A comprehensive 2-hour hands-on learning experience with OpenAI's Assistant API, featuring structured outputs, RAG with built-in `file_search`, and practical Python implementations.

## Quick Start

1. **Clone and setup**:

   ```bash
   git clone <your-repo-url>
   cd disctrai
   pip install -r requirements.txt
   ```

2. **Configure API access**:

   ```bash
   cp .env.example .env
   # Edit .env with your OPENAI_API_KEY
   ```

3. **Run the labs**:
   ```bash
   python scripts/00_bootstrap.py      # Bootstrap assistant
   python scripts/01_responses_api.py       # Threads → Runs → streaming
   python scripts/02_structured_output.py   # JSON-mode + function tools
   python scripts/03_rag_file_search.py     # End-to-end RAG
   python scripts/99_cleanup.py            # Clean up resources
   ```

## Repository Structure

```
openai-practice-lab/
│
├─ README.md              # This file - Quick-start & roadmap
├─ requirements.txt       # openai>=1.83.0, python-dotenv, pydantic, pytest
├─ .env.example           # OPENAI_API_KEY, OPENAI_ORG (optional)
│
├─ scripts/
│   ├─ 00_init_assistant.py      # Helper: creates or updates one reusable assistant
│   ├─ 01_responses_api.py       # Walk-through of Threads → Runs → streaming
│   ├─ 02_structured_output.py   # JSON-mode + function tools demo
│   ├─ 03_rag_file_search.py     # End-to-end RAG with `file_search`
│   └─ 99_cleanup.py            # Delete test threads, files, runs
│
├─ data/                         # Sample PDFs / Markdown to upload
│
└─ tests/
    └─ test_runs.py              # pytest sanity checks (<5 min)
```

## completeness

```ssh
❯ python3 scripts/00_bootstrap.py

✅ Assistant создан.
Assistant ID: asst_srDrauPRaU54XIhJxXhlsoy2
```

Part1:
It works but i always see deprication (I think due to the older version functions)
```ssh
📄 File uploaded. File ID: file-BLGCK9tYGX7eos34zYmCpN
/home/maxim-sarsekeyev/nfactorial/discStrAi/scripts/01_qna_assistant.py:18: DeprecationWarning: The Assistants API is deprecated in favor of the Responses API
  thread = client.beta.threads.create()
/home/maxim-sarsekeyev/nfactorial/discStrAi/scripts/01_qna_assistant.py:21: DeprecationWarning: The Assistants API is deprecated in favor of the Responses API
  client.beta.threads.messages.create(
/home/maxim-sarsekeyev/nfactorial/discStrAi/scripts/01_qna_assistant.py:28: DeprecationWarning: The Assistants API is deprecated in favor of the Responses API
  run = client.beta.threads.runs.create(
⏳ Waiting for response...
/home/maxim-sarsekeyev/nfactorial/discStrAi/scripts/01_qna_assistant.py:37: DeprecationWarning: The Assistants API is deprecated in favor of the Responses API
  run = client.beta.threads.runs.retrieve(

📘 Response:
/home/maxim-sarsekeyev/nfactorial/discStrAi/scripts/01_qna_assistant.py:44: DeprecationWarning: The Assistants API is deprecated in favor of the Responses API
  messages = client.beta.threads.messages.list(thread_id=thread.id)
```
