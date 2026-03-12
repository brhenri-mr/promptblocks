from typing import Optional
from .section import Section
from .rule import Rule, Weight
from .example import Example


class Step(Section):
    """
    A single stage of reasoning or instruction within a prompt.

    A prompt with 8 stages has 8 steps. Each step has a title,
    an objective, and can contain rules and examples.
    """

    def __init__(
        self,
        title: str,
        objective: str,
        rules: Optional[list[Rule]] = None,
        examples: Optional[list[Example]] = None,
        sort_rules_by_weight: bool = False,
    ):
        self.title = title
        self.objective = objective
        self.rules = rules or []
        self.examples = examples or []
        self.sort_rules_by_weight = sort_rules_by_weight

    def render(self, **context) -> str:
        lines = []

        title = self._interpolate(self.title, context)
        lines.append(f"### {title}")
        lines.append("")

        objective = self._interpolate(self.objective, context)
        lines.append(objective)

        if self.rules:
            lines.append("")
            lines.append("**Rules:**")

            rules = self.rules
            if self.sort_rules_by_weight:
                rules = sorted(self.rules, key=lambda r: r.weight.order())

            for rule in rules:
                lines.append(f"- {rule.render(**context)}")

        if self.examples:
            lines.append("")
            lines.append("**Examples:**")
            for example in self.examples:
                lines.append(f"- {example.render(**context)}")

        return "\n".join(lines)