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
``` this version used assistant and threads

if using just response there is no warning and simple warning( which is in older commit)

### How it Works:
1. **Existence**: The theorem guarantees that there is a number \( x \) that satisfies all the given congruences simultaneously.

2. **Uniqueness**: The solution \( x \) is unique modulo \( N \), where \( N \) is the product of all the moduli.

3. **Finding the Solution**:
   - Compute \( N_i = N / n_i \) for each \( i \).
   - Find the multiplicative inverse \( y_i \) of \( N_i \) modulo \( n_i \).
   - The solution \( x \) can be constructed using the formula:
     \[
     x \equiv \sum_{i=1}^k a_i \cdot N_i \cdot y_i \ (\text{mod} \ N)
     \]

### Example:
Consider the system of congruences:
\[ 
x \equiv 2 \ (\text{mod} \ 3) \\
x \equiv 3 \ (\text{mod} \ 4) \\
x \equiv 1 \ (\text{mod} \ 5) 
\]

To solve, find \( N = 3 \times 4 \times 5 = 60 \). Then compute:
- \( N_1 = 60 / 3 = 20 \)
- \( N_2 = 60 / 4 = 15 \)
- \( N_3 = 60 / 5 = 12 \)

Next, calculate the modular inverses:
- \( y_1 \equiv 20^{-1} \ (\text{mod} \ 3) \)
- \( y_2 \equiv 15^{-1} \ (\text{mod} \ 4) \)
- \( y_3 \equiv 12^{-1} \ (\text{mod} \ 5) \)

Finally, substitute into the formula to find \( x \). This will yield a solution that satisfies all congruences simultaneously.

The Chinese Remainder Theorem is powerful for computations in modular arithmetic, cryptography, and computer science.


Part 2: Notes
```ssh
❯ python3 scripts/02_generate_notes.py

{
  "notes": [
    "Understand the main concepts of the study material for comprehensive coverage.",
    "Prioritize key terms and their definitions that frequently appear in exams.",
    "Review past exam papers to identify common question patterns and formats.",
    "Summarize each chapter into bullet points for quick revision.",
    "Create flashcards for important dates, formulas, and figures for effective recall.",
    "Group similar topics together to make connections and enhance retention.",
    "Practice problem-solving skills with sample problems or exercises from the study guide.",
    "Utilize mnemonic devices to remember complex information more easily.",
    "Discuss difficult concepts with peers to gain different perspectives and insights.",
    "Set a revision schedule that allows for regular review sessions leading up to the exam."
  ]
}
1. Note 1 (page None)
  Understand the main concepts of the study material for comprehensive coverage.

2. Note 2 (page None)
  Prioritize key terms and their definitions that frequently appear in exams.

3. Note 3 (page None)
  Review past exam papers to identify common question patterns and formats.

4. Note 4 (page None)
  Summarize each chapter into bullet points for quick revision.

5. Note 5 (page None)
  Create flashcards for important dates, formulas, and figures for effective recall.

6. Note 6 (page None)
  Group similar topics together to make connections and enhance retention.

7. Note 7 (page None)
  Practice problem-solving skills with sample problems or exercises from the study guide.

8. Note 8 (page None)
  Utilize mnemonic devices to remember complex information more easily.

9. Note 9 (page None)
  Discuss difficult concepts with peers to gain different perspectives and insights.

10. Note 10 (page None)
  Set a revision schedule that allows for regular review sessions leading up to the exam.

```