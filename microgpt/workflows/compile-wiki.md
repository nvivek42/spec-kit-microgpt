name=.microgpt/workflows/compile-wiki.md
# Wiki compiler workflow spec

name: compile-wiki
summary: "Compile raw data into an Obsidian-friendly wiki. Summarize, backlink, and categorize documents."
inputs:
  - raw/
outputs:
  - wiki/

steps:
  - id: summarize
    description: "Generate a short summary (2-4 paragraphs) for each raw document."
  - id: extract_concepts
    description: "Extract a list of key concepts and tags per document."
  - id: backlinks
    description: "Generate backlink references between documents and create an index page per concept."
  - id: write_markdown
    description: "Write the compiled markdown files into wiki/ with local asset paths."

notes: |
  Implementations of this spec should use an LLM to produce the summaries and concept extraction, and may use simple heuristics for backlinking. Keep images local and reference them from wiki/assets/.
