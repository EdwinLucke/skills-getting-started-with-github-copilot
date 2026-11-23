# Activities API Specification

## Scope

The API serves extracurricular activity information and lets students register for activities. Activity data is held in memory and resets when the application restarts.

Each activity has:

- `description`: a short description.
- `schedule`: when the activity meets.
- `max_participants`: the activity's listed capacity.
- `participants`: the email addresses currently registered.

## Endpoints

### `GET /`

Redirect to `/static/index.html`.

### `GET /activities`

Return HTTP `200` with a JSON object keyed by activity name. Each activity value contains the four fields listed above.

### `POST /activities/{activity_name}/signup?email={email}`

Register the supplied email for the named activity.

- If the activity exists and the email is not registered, append the email to `participants` and return HTTP `200` with `{"message": "Signed up {email} for {activity_name}"}`.
- If the activity does not exist, return HTTP `404` with `{"detail": "Activity not found"}`.
- If the email is already registered for that activity, return HTTP `400` with `{"detail": "Student already signed up for this activity"}` and do not change the participant list.
- If `email` is omitted, return HTTP `422` for the missing required query parameter.

### `DELETE /activities/{activity_name}/signup?email={email}`

Unregister the supplied email from the named activity.

- If the activity exists and the email is registered, remove that email from `participants` and return HTTP `200` with `{"message": "Unregistered {email} from {activity_name}"}`.
- If the activity does not exist, return HTTP `404` with `{"detail": "Activity not found"}`.
- If the email is not registered for the activity, return HTTP `404` with `{"detail": "Student is not signed up for this activity"}`.
- If `email` is omitted, return HTTP `422` for the missing required query parameter.

## State and Scope Notes

- Registrations are stored in the application's in-memory activity data; they are not persisted across restarts.
- The `max_participants` field is returned as activity information. Capacity enforcement is not specified by this API contract.
- Authentication and authorization are not implemented; the API is intended for demo use only.
