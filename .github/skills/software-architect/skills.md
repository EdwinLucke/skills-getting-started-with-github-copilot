---
name: software-architecture
description: Software architecture guidance for designing, evaluating, and evolving applications and distributed systems. Use for system design, component boundaries, APIs, data, security, scalability, reliability, cloud, and technical decision records.
---

# Software Architecture

## Purpose

Provide practical architecture guidance that aligns technical decisions with business goals, constraints, and operational needs.

## Common Architecture Areas

Consider the areas relevant to the request:

- **Requirements and constraints:** user and business goals, functional requirements, quality attributes, budget, timeline, existing systems, and technology constraints.
- **System structure:** architecture style, component responsibilities, boundaries, dependencies, and ownership.
- **APIs and integration:** contracts, versioning, synchronous and asynchronous communication, external dependencies, and failure handling.
- **Data architecture:** ownership, persistence, consistency, access patterns, retention, migration, and privacy.
- **Security:** identity, access control, secrets, trust boundaries, threat considerations, and sensitive data handling.
- **Scalability and performance:** workload characteristics, bottlenecks, capacity, caching, and measured performance needs.
- **Reliability and operations:** availability, graceful degradation, recovery, observability, deployment, and incident response.
- **Delivery and evolution:** implementation sequencing, compatibility, migration strategy, and future change costs.

## Instructions

When asked to design or review an architecture:

1. Establish the business goal, scope, users, and important constraints.
2. Identify the quality attributes that matter most and any measurable targets.
3. Use the existing system and repository patterns as context; avoid proposing unnecessary rewrites or complexity.
4. Describe the key components, their responsibilities, and how they communicate.
5. Explain data ownership and important flows across system boundaries.
6. Evaluate relevant security, reliability, scalability, performance, and operational concerns.
7. Compare reasonable alternatives when the choice has meaningful trade-offs. State assumptions and uncertainties.
8. Recommend an incremental implementation or migration path when applicable.
9. Keep recommendations actionable and proportionate to the system's needs.

## Output Format

Adapt the sections to the task. Omit sections that do not apply.

### Summary

State the recommended direction and the main reason for it.

### Context and Constraints

Summarize relevant goals, requirements, constraints, and assumptions.

### Proposed Design

Describe the components, responsibilities, interfaces, and key data flows. Use a diagram when it clarifies the design.

### Decisions and Trade-offs

Explain important choices, alternatives considered, and their consequences.

### Risks and Mitigations

Identify material technical or operational risks and practical mitigations.

### Implementation Plan

List a sensible sequence of steps, including migration and validation where needed.

## Quality Standards

Always:

- Prefer the simplest design that meets the stated requirements.
- Distinguish confirmed facts from assumptions.
- Make trade-offs and operational consequences explicit.
- Consider security, privacy, reliability, maintainability, and total cost where relevant.
- Avoid prescribing technologies without a requirement or constraint that supports the choice.