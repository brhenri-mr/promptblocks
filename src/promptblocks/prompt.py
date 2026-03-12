from typing import Optional
from .step import Step
from .renderer import Renderer


class Prompt:
    """
    The top-level container for a structured prompt.

    Holds all steps in order and is responsible for rendering
    the final string. Accepts dynamic variables at render time,
    which are propagated to every block inside it.
    """

    def __init__(self, title: str = "", steps: Optional[list[Step]] = None):
        self.title = title
        self._steps: list[Step] = steps or []
        self._renderer = Renderer()

    def add(self, step: Step) -> "Prompt":
        """Add a step to the prompt. Returns self for chaining."""
        self._steps.append(step)
        return self

    def render(self, **context) -> str:
        """
        Render the full prompt as a string.

        All context variables are propagated to every step,
        rule, and example inside this prompt.
        """
        if not self._steps:
            raise ValueError("Cannot render a prompt with no steps.")

        return self._renderer.render(self.title, self._steps, **context)

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"Prompt(title={self.title!r}, steps={len(self._steps)})"

    @property
    def steps(self):
        '''
        Return the prompt steps
        '''
        return [f'{i+1} Step - {el.title}' for i, el in enumerate(self._steps)]

    