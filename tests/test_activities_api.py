from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(app_module.activities))
    return TestClient(app_module.app)


def test_root_redirects_to_activity_page(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_activity_details(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert all(
        {"description", "schedule", "max_participants", "participants"} <= activity.keys()
        for activity in activities.values()
    )


def test_signup_adds_email_to_activity(client):
    email = "student@mergington.edu"

    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}
    assert email in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_rejects_duplicate_registration_without_changing_participants(client):
    email = "student@mergington.edu"
    endpoint = "/activities/Chess%20Club/signup"
    first_response = client.post(endpoint, params={"email": email})
    participants_before_duplicate = client.get("/activities").json()["Chess Club"]["participants"]

    duplicate_response = client.post(endpoint, params={"email": email})

    assert first_response.status_code == 200
    assert duplicate_response.status_code == 400
    assert duplicate_response.json() == {
        "detail": "Student already signed up for this activity"
    }
    participants_after_duplicate = client.get("/activities").json()["Chess Club"]["participants"]
    assert participants_after_duplicate == participants_before_duplicate


def test_signup_returns_not_found_for_unknown_activity(client):
    response = client.post(
        "/activities/Unknown%20Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_requires_email(client):
    response = client.post("/activities/Chess%20Club/signup")

    assert response.status_code == 422
