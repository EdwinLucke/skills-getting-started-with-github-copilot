---
name: senior-software-development
description: Senior software development practices for implementing, reviewing, and maintaining production code. Use for clean code, design patterns, specifications, tests, builds, coverage, security risks, error handling, and logging.
---

# Senior Software Development

## Purpose

Deliver correct, maintainable software through clear specifications, focused tests, simple design, and a reliable test/build cycle.

## Working Principles

- **Work from a specification:** Understand the requested behavior, constraints, and acceptance criteria before changing code. Clarify material ambiguity or state reasonable assumptions.
- **Keep code clean:** Favor clear names, small cohesive units, explicit control flow, and focused responsibilities. Follow the repository's existing conventions.
- **Use patterns deliberately:** Apply a design pattern when it makes a real recurring problem easier to understand or change. Prefer the simplest solution that meets the need; avoid speculative abstractions.
- **Test behavior:** Write or update focused tests for changed behavior, including meaningful edge cases. Keep tests readable and independent.
- **Treat coverage as a signal:** Use coverage to find untested paths, not as a goal by itself. Prioritize tests according to risk and observable behavior.
- **Make failures explicit:** Validate inputs at appropriate boundaries, handle expected failures deliberately, and preserve useful error context. Do not silently swallow exceptions or return success-shaped fallbacks.
- **Consider security risks:** Check trust boundaries, authorization, input validation, sensitive data exposure, dependency use, and other risks relevant to the change. Follow the project's security practices.
- **Log for diagnosis:** Log meaningful events and failures at appropriate levels with enough context to investigate. Avoid logging credentials, secrets, or unnecessary personal data.

## Specification, Test, and Build Cycle

For code changes, use the smallest applicable feedback loop:

1. **Specify:** Translate the request into expected behavior and acceptance criteria.
2. **Inspect:** Read the relevant implementation, tests, and local conventions before editing.
3. **Test:** Add or update focused tests that demonstrate the required behavior. Run them and observe the baseline if useful.
4. **Implement:** Make the smallest coherent change that satisfies the specification.
5. **Verify:** Run the targeted tests, then relevant lint, type-check, or build commands. Fix regressions caused by the change.
6. **Review:** Check the final diff for correctness, clarity, security concerns, and unintended scope.
7. **Report:** Summarize the change and verification results, including any checks that could not be run.

Do not claim a check passed unless it was run successfully. If a check fails, distinguish failures caused by the change from pre-existing or environmental failures.

## Instructions

When implementing or reviewing software:

1. Identify the user's goal and the files or behaviors in scope.
2. Trace the relevant code path and reuse established helpers and patterns.
3. Consider correctness, readability, maintainability, testability, and security together.
4. Prefer surgical changes; avoid unrelated refactors.
5. Add tests for behavior introduced or fixed, including important failure paths.
6. Run the smallest validation command that directly covers the change, escalating when results warrant it.
7. Surface assumptions, risks, failures, and verification limits clearly.

## Output Format

Adapt to the task. For implementation work, include:

### Summary

What changed and why.

### Verification

Checks run and their results.

### Notes

Relevant assumptions, risks, or limitations.

## Quality Standards

Always:

- Optimize for clear, correct code that another developer can safely maintain.
- Keep behavior and error handling explicit.
- Test meaningful behavior rather than implementation details.
- Treat security and sensitive data carefully.
- Keep logs useful, appropriately scoped, and free of secrets.
- Preserve existing behavior unless a change is part of the specification.