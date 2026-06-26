 #!/usr/bin/env python3
 """Lightweight hybrid search for a customer knowledge-base vault.

 Zero external dependencies. Combines BM25-like term scoring with path/title
 boosts and emits JSON for agent consumption. Drop into any customer root and
 run: python hybrid_search.py "关键词" --root .
 """

 from __future__ import annotations

 import argparse
 import json
 import math
 import re
 from dataclasses import dataclass
 from pathlib import Path
 from typing import Iterable


 # Generic exclusions that apply to most knowledge-base roots.
 EXCLUDED_DIRS = {".git", ".obsidian", ".tmp", "node_modules", "__pycache__"}
 DEFAULT_TOP_K = 10


 @dataclass
 class Document:
     path: Path
     title: str
     text: str
     tokens: list[str]


 def tokenize(text: str) -> list[str]:
     # Keep Chinese character runs and latin/number tokens. This is a pragmatic
     # tokenizer for mixed Chinese/English vault content.
     return [token.lower() for token in re.findall(r"[\u4e00-\u9fff]+|[a-zA-Z0-9_\-]+", text)]


 def iter_markdown_files(root: Path) -> Iterable[Path]:
     for path in root.rglob("*.md"):
         rel_parts = path.relative_to(root).parts
         if any(part in EXCLUDED_DIRS for part in rel_parts):
             continue
         yield path


 def read_document(root: Path, path: Path) -> Document:
     text = path.read_text(encoding="utf-8", errors="ignore")
     title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
     title = title_match.group(1).strip() if title_match else path.stem
     rel_text = str(path.relative_to(root)).replace("\\", "/")
     combined = f"{title}\n{rel_text}\n{text}"
     return Document(path=path, title=title, text=text, tokens=tokenize(combined))


 def build_corpus(root: Path) -> list[Document]:
     return [read_document(root, path) for path in iter_markdown_files(root)]


 def score_documents(root: Path, docs: list[Document], query: str) -> list[dict]:
     query_tokens = tokenize(query)
     if not query_tokens:
         return []

     doc_freq: dict[str, int] = {}
     for doc in docs:
         unique_tokens = set(doc.tokens)
         for token in query_tokens:
             if token in unique_tokens:
                 doc_freq[token] = doc_freq.get(token, 0) + 1

     avg_len = sum(len(doc.tokens) for doc in docs) / max(len(docs), 1)
     results: list[dict] = []

     for doc in docs:
         token_counts: dict[str, int] = {}
         for token in doc.tokens:
             token_counts[token] = token_counts.get(token, 0) + 1

         bm25 = 0.0
         for token in query_tokens:
             tf = token_counts.get(token, 0)
             if tf == 0:
                 continue
             df = doc_freq.get(token, 0)
             idf = math.log(1 + (len(docs) - df + 0.5) / (df + 0.5))
             k1 = 1.5
             b = 0.75
             denom = tf + k1 * (1 - b + b * len(doc.tokens) / max(avg_len, 1))
             bm25 += idf * (tf * (k1 + 1)) / denom

         rel_path = str(doc.path.relative_to(root)).replace("\\", "/")
         title_text = doc.title.lower()
         path_text = rel_path.lower()
         title_boost = sum(1.5 for token in query_tokens if token in title_text)
         path_boost = sum(0.8 for token in query_tokens if token in path_text)
         score = bm25 + title_boost + path_boost

         if score <= 0:
             continue

         snippet = make_snippet(doc.text, query_tokens)
         results.append(
             {
                 "path": rel_path,
                 "title": doc.title,
                 "score": round(score, 4),
                 "snippet": snippet,
             }
         )

     results.sort(key=lambda item: item["score"], reverse=True)
     return results


 def make_snippet(text: str, query_tokens: list[str], width: int = 140) -> str:
     compact = re.sub(r"\s+", " ", text).strip()
     lower = compact.lower()
     first_hit = min((lower.find(token) for token in query_tokens if lower.find(token) >= 0), default=0)
     start = max(0, first_hit - width // 3)
     return compact[start : start + width]


 def main() -> None:
     parser = argparse.ArgumentParser(description="Search markdown files with a lightweight hybrid scorer.")
     parser.add_argument("query", help="Search query")
     parser.add_argument("--root", default=".", help="Vault root, defaults to current directory")
     parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K, help="Number of results")
     args = parser.parse_args()

     root = Path(args.root).resolve()
     docs = build_corpus(root)
     results = score_documents(root, docs, args.query)[: args.top_k]
     print(json.dumps({"query": args.query, "count": len(results), "results": results}, ensure_ascii=False, indent=2))


 if __name__ == "__main__":
     main()
