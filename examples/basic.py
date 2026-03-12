from promptblocks import Prompt, Step, Rule, Weight, Good, Bad

# This example mirrors a real-world prompt with multiple stages,
# weighted rules, and good/bad examples — the kind that usually
# ends up as a 500-line f-string.

prompt = Prompt(title="Document Analysis Agent")

prompt.add(Step(
    title="Context Understanding",
    objective="Analyze the context of the information provided in {document_type}.",
    rules=[
        Rule("Never invent or assume data not present in the source", weight=Weight.HIGH),
        Rule("Always identify the document language before proceeding", weight=Weight.HIGH),
        Rule("If context is ambiguous, flag it explicitly", weight=Weight.MEDIUM),
    ],
    examples=[
        Good("Document is a legal contract in Portuguese → flag language, proceed"),
        Bad("Document language is unknown → assume English and proceed silently"),
    ],
    sort_rules_by_weight=True,
))

prompt.add(Step(
    title="Entity Extraction",
    objective="Extract all named entities relevant to {extraction_target}.",
    rules=[
        Rule("Extract only entities explicitly mentioned", weight=Weight.HIGH),
        Rule("Normalize dates to ISO 8601 format", weight=Weight.MEDIUM),
        Rule("Group entities by type: person, organization, location", weight=Weight.LOW),
    ],
))

prompt.add(Step(
    title="Output Formatting",
    objective="Format the extracted data according to the schema provided.",
    rules=[
        Rule("Return only valid JSON", weight=Weight.HIGH),
        Rule("Do not include fields not present in the schema", weight=Weight.HIGH),
        Rule("Use null for missing optional fields, never omit them", weight=Weight.MEDIUM),
    ],
    examples=[
        Good('{"name": "João Silva", "role": null}'),
        Bad('{"name": "João Silva"}  # missing required field'),
    ],
))

if __name__ == "__main__":
    result = prompt.render(
        document_type="legal contract",
        extraction_target="parties and obligations",
    )
    print(result)
    