import re
from abc import ABC, abstractmethod


class Section(ABC):
    """Base class for all prompt building blocks."""

    @abstractmethod
    def render(self, **context) -> str:
        """Render this section into a string, interpolating context variables."""
        raise NotImplementedError

    def _interpolate(self, text: str, context: dict) -> str:
        """
        Replace {variable} placeholders with context values.

        Only replaces tokens that are simple Python identifiers like {name}
        or {document_type}. Anything else — JSON snippets, quoted strings,
        expressions — is left untouched.
        """
        def replace(match):
            key = match.group(1)
            if key in context:
                return str(context[key])
            raise ValueError(f"Missing context variable: '{key}'")

        return re.sub(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}", replace, text)