from enum import Enum
from .section import Section


class Weight(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def label(self) -> str:
        labels = {
            Weight.HIGH: "HIGH",
            Weight.MEDIUM: "MEDIUM",
            Weight.LOW: "LOW",
        }
        return labels[self]

    def order(self) -> int:
        order = {
            Weight.HIGH: 0,
            Weight.MEDIUM: 1,
            Weight.LOW: 2,
        }
        return order[self]


class Rule(Section):
    """A single constraint or instruction within a step."""

    def __init__(self, content: str, weight: Weight = Weight.MEDIUM):
        self.content = content
        self.weight = weight

    def render(self, **context) -> str:
        interpolated = self._interpolate(self.content, context)
        return f"[{self.weight.label()}] {interpolated}"