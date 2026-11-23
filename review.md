# Project Review

Reviewed through the quality engineering, senior development, software architecture, service-level engineering, and customer-journey test engineering lenses in `.github/skills`.

## Summary

The app is small and understandable for a demo, and its API tests pass. The main risks to address before production use are participant privacy, registration integrity, and unclear capacity behavior. The current tests cover the Python API but not the frontend customer journey or service-level behavior.

## Findings

### High: Participant privacy and enrollment authorization

[`GET /activities`](./src/app.py#L87) returns participant email addresses, and [`signup_for_activity`](./src/app.py#L92) accepts registrations without authentication or identity verification. For a school app, this exposes student information and allows signups on someone else's behalf.

Before public deployment, restrict access to student data, verify a student's identity and eligibility, and avoid returning email addresses unless the user is authorized to see them.

### High: Registration state is volatile and duplicate checks are not atomic

The duplicate check and participant append are separate operations ([check](./src/app.py#L101), [append](./src/app.py#L105)); concurrent requests can both pass the check. The in-memory store also loses registrations on restart and can diverge across multiple workers.

For production use, store registrations durably and enforce uniqueness transactionally, for example with a unique constraint on activity and normalized student identity.

### Product decision: Capacity is displayed but not enforced

The UI calculates remaining spots ([`app.js`](./src/static/app.js#L24)), but the API accepts signups regardless of `max_participants`. The API specification explicitly says capacity enforcement is out of scope ([activities-api.md](./specs/activities-api.md#L36)).

Confirm whether capacity is informational or a real limit. If it is a limit, enforce it atomically in the API and test registration at capacity and attempts to exceed it.

### Medium: Validation relies on the browser

The API accepts `email` as a plain string ([`app.py`](./src/app.py#L92)); the HTML email input validates only normal browser submissions ([`index.html`](./src/static/index.html#L29)). Add server-side validation and define how email case and whitespace should be handled for duplicate detection.

### Medium: Feedback needs accessibility and styling polish

The feedback element has no live announcement for assistive technology ([`index.html`](./src/static/index.html#L40)). Also, setting `className` to `success` or `error` ([`app.js`](./src/static/app.js#L100)) drops the `message` class, so its padding and margin styles do not apply ([`styles.css`](./src/static/styles.css#L150)).

Use an appropriate live region or alert role and preserve the base message class when setting success or error state.

### Testing and service-level gaps

The six tests cover API behavior ([test_activities_api.py](./tests/test_activities_api.py#L15)). Python API line coverage is 100%, but there are no automated customer-journey tests for UI accessibility, network failures, concurrency, or capacity. There is also no telemetry or defined availability, latency, or error-rate objective, so service-level readiness cannot yet be assessed.

Add focused UI journey tests for critical flows and failure states. For a deployed service, define user-centered SLIs and establish SLO targets from measured baselines and business requirements.

## Verification

- `pytest -q`: 6 passed.
- Coverage for `src/app.py`: 100% (24 statements, 0 missed). This does not measure the frontend.
- The test run emitted one Starlette/httpx deprecation warning.
