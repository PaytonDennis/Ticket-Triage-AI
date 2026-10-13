# Support Ticket Triage AI

A Python service that uses Claude to triage customer support tickets for a fictional medical device company.
All data is fictional.

> Work in progress. Currently at **Stage 1: terminal chat loop**.

## Setup

Requires Python 3.11+.

```bash
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then put your real ANTHROPIC_API_KEY in .env
```

## Run the chat loop

```bash
python chat.py
```

Type `quit` to exit.
