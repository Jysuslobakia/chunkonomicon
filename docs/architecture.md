# Architecture and design rationale

## Why source-agnostic?

Commercial language-learning textbooks are protected by copyright. Their specific text is protected expression. Their organizational pattern (lesson -> dialogue -> vocabulary -> grammar point -> exercise) is a pedagogical method, not protected expression (idea-expression dichotomy).

chunkonomicon operates on that structural pattern, not on any single book's content. The repo ships only pipeline code, the generic lesson schema, and a synthetic sample corpus.

## Bring Your Own Textbook (BYOT)

Users who own a legal copy point TEXTBOOK_PDF_PATH at their own PDF. Nothing derived from it is committed, see .gitignore.

## Pipeline stages

1. Ingestion: extract text+layout, normalize into schema (dialogue, vocab_list, grammar_point, exercise, cultural_note).
2. Chunking: split along structural boundaries first, then recursively within long blocks.
3. Retrieval: embed, index, retrieve.
4. Generation: grounded prompt + LLM call.
5. Evaluation: RAGAS and DeepEval against a golden dataset.
