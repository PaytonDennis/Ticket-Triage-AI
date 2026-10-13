# Ticket Triage AI 🚧

> **Status:** Work in progress. Currently building Stage 1 (chat loop).

An AI agent that triages customer support tickets for a fictional medical device company.
It reads incoming tickets, classifies and prioritizes them, looks up customer data through
tool calls, searches a support knowledge base, and drafts replies with citations for a
human agent to approve.

## Planned features
- [ ] Chat loop with conversation history and system prompt
- [ ] `POST /triage` API with validated structured output
- [ ] Tool calling for account and order lookups
- [ ] Knowledge base search (RAG) with cited answers
- [ ] Human approval workflow for drafted replies
- [ ] Automated evals measuring triage accuracy, latency, and cost
- [ ] Docker + live deployment

## Tech stack
Python · FastAPI · Pydantic · Anthropic Claude API · SQLite · ChromaDB · pytest · Docker

*All customer data in this project is fictional.*
