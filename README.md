name=README.md
# spec-kit-microgpt

A small project that uses the spec-kit patterns to build a microGPT-powered personal knowledge base pipeline.

This repository is a scaffold created to follow the Spec-Driven Development approach from github/spec-kit and to integrate Andrej Karpathy's microgpt gist as a data source.

High-level structure

- raw/ — original source files (microgpt downloader placed here)
- .microgpt/ — workflow specs and LLM context for the wiki compiler
- wiki/ — compiled markdown/wiki output (Obsidian-friendly)
- src/specify_cli/integrations/microgpt/ — integration stub following spec-kit patterns
- scripts/ — utility scripts to update agent context and run tasks

Quick start

1. Clone the repo:
   git clone https://github.com/nvivek42/spec-kit-microgpt.git
   cd spec-kit-microgpt

2. (Optional) Create a Python virtual environment and install dev tools:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt

3. Download the microgpt source into raw/:
   python raw/microgpt.py --fetch

4. Open .microgpt/workflows/compile-wiki.md to customize the compilation spec and then run the implementation when it's ready.

What I scaffolded

- Initial project skeleton and integration stubs to plug into spec-kit patterns.
- A workflow spec and LLM context template for the wiki compiler.
- A downloader that fetches the Karpathy microgpt gist raw file into raw/microgpt_raw.py.

Next steps

- Implement the compile runner (Python script or SkillsIntegration) that reads raw/, calls an LLM, and writes compiled markdown into wiki/.
- Add an indexing/retrieval component (embedding-based or inverted-index) for Q&A.
- Wire up CI and add tests.

If you'd like, I can now implement the compile runner and a basic query CLI using a simple retrieval strategy. Reply with which LLM you'd like (OpenAI/local) and whether you want embeddings (FAISS) or a lightweight keyword retrieval.
