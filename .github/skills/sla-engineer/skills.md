---
name: service-level-engineering
description: Service-level engineering guidance for defining and improving SLAs, SLOs, and SLIs. Use for availability, latency, throughput, error rates, capacity, monitoring, incidents, and reliability reporting.
---

# Service-Level Engineering

## Purpose

Help teams define measurable service expectations and improve performance, availability, and operational reliability using evidence-based targets.

## Core Concepts

- **Service-level indicator (SLI):** A clearly defined measurement of user-facing service behavior, such as successful request rate or request latency.
- **Service-level objective (SLO):** A target for an SLI over a stated measurement window.
- **Service-level agreement (SLA):** A commitment to customers that defines scope, measurement, exclusions, reporting, and any consequences when commitments are missed.
- **Error budget:** The permitted unreliability implied by an SLO over its measurement window. Use it to inform delivery and reliability trade-offs.

Keep these concepts distinct. An internal SLO can be stricter than a customer-facing SLA.

## Common Areas

Consider the areas relevant to the service:

- **Availability:** Successful, eligible user operations over a defined period; document which requests and failures count.
- **Latency and performance:** Response-time distributions, especially tail percentiles, under representative load.
- **Errors:** User-visible failures, timeouts, dependency failures, and retry outcomes; distinguish expected client errors from service failures.
- **Throughput and capacity:** Request volume, saturation, resource headroom, scaling behavior, and performance under peak or burst load.
- **Reliability and recovery:** Failure domains, graceful degradation, redundancy, backup and restore, and recovery objectives.
- **Observability:** SLIs, logs, traces, dashboards, alert thresholds, data quality, and ownership.
- **Incidents and operations:** Detection, escalation, communication, mitigation, recovery, and learning from incidents.
- **Service boundaries:** Dependencies, regions, customer tiers, maintenance windows, and third-party services that affect measurement or commitments.

## Instructions

When asked to define, assess, or improve service levels:

1. Establish the service boundary, user journeys, customer commitments, and business impact of failure.
2. Identify measurable, user-centered SLIs. Define the numerator, denominator, eligible population, event source, and aggregation method.
3. Propose SLO targets and measurement windows only when supported by requirements or evidence. State assumptions; do not invent contractual commitments.
4. Analyze availability, latency, errors, throughput, and capacity as applicable. Include peak load, dependency failures, and degraded modes.
5. Check whether telemetry can measure the proposed indicators accurately and consistently.
6. Design alerts around actionable symptoms and user impact; avoid paging on metrics that have no response plan.
7. Explain error-budget implications and how missed objectives should affect risk, release, or mitigation decisions.
8. For SLA language, make scope, exclusions, measurement window, reporting, and remedies explicit and suitable for appropriate business or legal review.
9. Recommend concrete validation, load testing, resilience testing, monitoring, and incident-response improvements.

## Output Format

Adapt the sections to the task. Avoid unsupported precision.

### Summary

State the service-level concern and recommended direction.

### Scope and Assumptions

Describe the service boundary, user impact, dependencies, and assumptions.

### SLIs and Targets

| Indicator | Definition | Target and window | Measurement source |
| --- | --- | --- | --- |
| Availability | Define eligible successful operations | Set from requirements or evidence | Identify telemetry source |

### Risks and Gaps

Describe reliability risks, measurement gaps, and likely user impact.

### Recommendations

List prioritized actions for performance, availability, error reduction, monitoring, and operations.

### Incident and Error-Budget Response

Explain alerting, escalation, mitigation, communication, and follow-up as relevant.

## Quality Standards

Always:

- Define what is measured and what is excluded.
- Prefer user-centered indicators over infrastructure-only proxies.
- Distinguish observed baselines, proposed objectives, and contractual guarantees.
- Use representative data and workload assumptions; report uncertainty.
- Make alerts actionable and assign clear ownership.
- Consider dependency behavior, graceful degradation, recovery, and customer communication.