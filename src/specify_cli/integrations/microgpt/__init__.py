name=src/specify_cli/integrations/microgpt/__init__.py
"""
Minimal MicroGPT integration stub for spec-kit patterns.
This file is a scaffold: adapt imports and base classes to match your spec-kit version.
"""

from typing import Dict

try:
    # The real spec-kit repo exposes integration base classes in specify_cli.integrations.base
    from specify_cli.integrations.base import MarkdownIntegration
except Exception:
    # Fallback stub for local testing
    class MarkdownIntegration:
        pass


class MicroGPTIntegration(MarkdownIntegration):
    """Integration to run the microgpt-based wiki compiler.
    This is a minimal scaffold. Implement `compile` or appropriate hooks to run the compile workflow.
    """

    key = "microgpt"
    config: Dict = {
        "name": "MicroGPT (downloader + compiler stub)",
        "folder": ".microgpt/",
        "commands_subdir": "workflows",
        "install_url": None,
        "requires_cli": False,
    }

    def compile(self, raw_dir: str = 'raw', wiki_dir: str = 'wiki'):
        """Run the compile workflow. This should be implemented to call an LLM and write markdown to wiki_dir."""
        raise NotImplementedError("Implement the compile runner to read raw/ and write wiki/")
