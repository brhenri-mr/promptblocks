# promptblocks

> Build large, structured LLM prompts the same way you build data models.


## What promptblocks Does

**promptblocks** gives your prompts the same structure and readability you expect from your Python code.

Instead of maintaining a monolithic string, you declare your prompt as a composition of meaningful building blocks — steps, rules, examples, context — each with its own place, its own weight, and its own responsibility.

The result is a prompt that you can read, navigate, extend, and version-control like any other piece of software.

## Core Concepts

### Prompt
The top-level container. Holds all steps in order and is responsible for rendering the final string. Accepts dynamic variables at render time, which are propagated to every block inside it.

### Step
Represents a single stage of reasoning or instruction. A prompt with 8 stages has 8 steps. Each step has a title, an objective, and can contain rules and examples.

### Rule
A single constraint or instruction within a step. Rules have content and an optional weight that signals their importance. Weight influences both how the rule is rendered and, optionally, its ordering.

### Weight
An enum that expresses the priority of a rule: `HIGH`, `MEDIUM`, or `LOW`. High-weight rules can be rendered more prominently or sorted to the top — the behavior is configurable.

### Example
An illustrative case attached to a step. Examples can be marked as `Good` or `Bad`, making the expected behavior explicit without hiding it in prose.

### Context (Section)
A free-form section that can be added to a step or directly to the prompt. Useful for dynamic content like retrieved documents, user input, or session state.

---

## Status

This project is in early design and development. The API is not stable. Feedback on the concepts and structure is very welcome.
