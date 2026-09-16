# chunkonomicon

Structure-aware RAG pipeline for language-learning textbooks: source-agnostic PDF ingestion, layout-aware chunking, and retrieval evaluation.

## What this is

`chunkonomicon` is not tied to any single textbook. It defines a generic **lesson schema** (dialogue, vocabulary list, grammar point, exercise) and a pipeline that extracts, normalizes, chunks, indexes, and retrieves content from any structured language-learning manual that follows that pattern (Genki, Minna no Nihongo, Tobira, etc.).

## Bring Your Own Textbook (BYOT)

This repository never ships copyrighted textbook content. Instead:

- `data/sample/` contains a small synthetic lesson used for demos, tests, and CI.
- To use your own legally owned textbook, copy the PDF into `data/raw/` (git-ignored) and point `TEXTBOOK_PDF_PATH` in your local `.env` to it.
- Nothing under `data/raw/`, `data/interim/`, or `data/processed/` is ever committed.

See `docs/architecture.md` for the full rationale and pipeline design.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m chunkonomicon.pipeline
```

## License

MIT for code only; does not cover third-party textbook content.
