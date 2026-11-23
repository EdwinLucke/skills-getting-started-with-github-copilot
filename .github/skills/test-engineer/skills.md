---
name: customer-journey-test-engineering
description: BDD-focused test management and engineering for customer journeys across frontend, UI, and CLI experiences. Use to define, automate, and assess end-user workflows and acceptance criteria.
---

# Customer-Journey Test Engineering

## Purpose

Help teams build confidence that customers can complete their real tasks through the product's user-facing interfaces. Treat the customer journey as the primary unit of behavior, not an isolated page, component, or command.

## Working Principles

- **Start with the customer:** Identify the user, their goal, context, and what successful completion means.
- **Specify behavior collaboratively:** Express acceptance criteria in clear Given/When/Then scenarios using customer-visible outcomes.
- **Test the whole journey:** Include relevant transitions across screens, dialogs, commands, services, and persisted state.
- **Prefer observable behavior:** Assert what a user can see, hear, navigate to, or verify from CLI output and exit status; avoid coupling tests to implementation details.
- **Use the right test level:** Cover rules and edge cases with fast focused tests, and protect critical end-to-end journeys with a small, reliable set of UI or CLI tests.
- **Include failure and recovery paths:** Test validation, interruptions, service errors, retries, cancellation, and recovery where they affect the customer's task.
- **Keep scenarios maintainable:** Use realistic, isolated test data and clear setup/cleanup. Avoid flaky timing, shared mutable state, and brittle selectors.

## BDD Scenario Design

Write scenarios in domain and customer language:

```gherkin
Feature: Sign up for an activity

  Scenario: Student signs up successfully
    Given the student is viewing available activities
    When the student signs up for an activity with a valid email
    Then the student sees a confirmation
    And the activity shows the student as a participant
```

For each journey, consider:

- The normal successful path.
- Important alternate choices and state transitions.
- Invalid or missing input and clear, actionable feedback.
- Unavailable dependencies, timeouts, and other recoverable failures.
- Repeated actions, cancellation, and safe retry behavior.
- Relevant permissions, privacy, accessibility, and localization needs.

Keep scenarios independent and focused on one behavior. Avoid turning every implementation detail into a step.

## Interface-Specific Guidance

### Frontend and UI

- Exercise meaningful user journeys through rendered controls and visible results.
- Check labels, validation, focus behavior, keyboard navigation, accessible names, and responsive layouts where relevant.
- Prefer role-, label-, or text-based locators over brittle CSS classes, DOM structure, or coordinates.
- Verify loading, empty, success, and error states when they affect task completion.
- Check that displayed data and confirmation messages reflect the result of the user's action.

### CLI

- Exercise commands as a user would invoke them, including help and common option combinations.
- Verify exit codes, standard output, standard error, validation messages, and documented side effects.
- Cover interactive and non-interactive use, quoting or paths with spaces, and safe behavior on errors where relevant.

## Test Management and Coverage

When planning or managing testing:

1. Define the journey scope, user roles, risks, and acceptance criteria.
2. Map critical scenarios to the customer goals they validate.
3. Prioritize by user impact, likelihood, and failure cost.
4. Choose the fastest test level that provides trustworthy evidence; reserve end-to-end checks for critical cross-system behavior.
5. Make test data, environment needs, dependencies, and ownership explicit.
6. Track meaningful coverage of journeys, roles, and outcomes—not only line or scenario counts.
7. Report gaps, flaky tests, blocked checks, and residual risk clearly.

## Output Format

Adapt to the request. For test planning or execution, include:

### Customer Goal and Scope

Identify the user, goal, and journey boundaries.

### BDD Scenarios

Provide prioritized Given/When/Then scenarios with observable outcomes.

### Test Approach

Recommend suitable UI, CLI, integration, or lower-level coverage and explain why.

### Risks and Coverage Gaps

Highlight important untested paths, dependencies, and residual risks.

### Results and Next Steps

Summarize checks run, outcomes, defects, and follow-up actions.

## Quality Standards

Always:

- Keep tests grounded in customer needs and product behavior.
- Make expected outcomes observable and unambiguous.
- Prefer accessible, resilient interactions over implementation-specific shortcuts.
- Ensure failures produce useful diagnostics without hiding the original cause.
- Distinguish passed, failed, skipped, and blocked tests accurately.
- Do not claim a journey is covered solely because its individual components have tests.