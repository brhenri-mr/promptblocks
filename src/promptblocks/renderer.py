from .step import Step


class Renderer:
    """
    Responsible for transforming a list of Steps into a final string.

    Keeping rendering logic isolated here means that supporting
    different output formats (Markdown, XML, plain text) in the
    future only requires changes in this file.
    """

    def render(self, title: str, steps: list[Step], **context) -> str:
        lines = []

        if title:
            lines.append(f"# {title}")
            lines.append("")

        for index, step in enumerate(steps, start=1):
            step_title = step._interpolate(step.title, context)
            lines.append(f"## Step {index} — {step_title}")
            lines.append("")
            lines.append(step.render(**context))
            lines.append("")

        return "\n".join(lines).strip()