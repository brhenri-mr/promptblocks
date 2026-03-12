from .section import Section


class Example(Section):
    """Base class for prompt examples."""

    def __init__(self, content: str):
        self.content = content

    def render(self, **context) -> str:
        raise NotImplementedError


class Good(Example):
    """An example of correct or expected behavior."""

    def render(self, **context) -> str:
        interpolated = self._interpolate(self.content, context)
        return f"✅ {interpolated}"


class Bad(Example):
    """An example of incorrect or undesired behavior."""

    def render(self, **context) -> str:
        interpolated = self._interpolate(self.content, context)
        return f"❌ {interpolated}"