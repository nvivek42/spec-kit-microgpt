name=.microgpt/context/compile-rules.md
# LLM context & rules for the wiki compiler

Purpose: Instruct the LLM to convert raw documents into well-structured Obsidian markdown articles.

Rules:

1. Output format
   - Title: Use a single H1 line (# Title)
   - Summary: a single short paragraph (2-4 sentences)
   - Body: sections using H2 headings, include code blocks in fenced markdown when appropriate.
   - Metadata: at the top include a YAML frontmatter with fields: source_filename, concepts (list), backlinks (list)

2. Backlinks
   - When two documents reference the same concept, add each other to backlinks list.

3. Images
   - If the raw document references images, save images to wiki/assets/<slug>/ and update the image links accordingly.

4. Concepts and tags
   - Produce a short list of 3-10 concepts that summarize the main ideas in the document. Prefer concise single-word or short-phrase concepts.

5. Citations
   - For web articles, include a source URL in frontmatter as source_url.

Prompt template (implementation should substitute the raw file contents and desired output path):

"""
You are an assistant that converts a raw text document into a structured Obsidian markdown article. Follow the rules above precisely. Input follows:

---
{raw_text}
---

Return the resulting markdown content only.
"""
