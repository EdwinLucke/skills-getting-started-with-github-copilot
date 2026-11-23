from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(app_module.activities))
    return TestClient(app_module.app)


def test_root_redirects_to_activity_page(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_activity_details(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert all(
        expected_fields <= activity.keys()
        for activity in activities.values()
    )


def test_signup_adds_email_to_activity(client):
    # Arrange
    email = "student@mergington.edu"
    expected_message = f"Signed up {email} for Chess Club"

    # Act
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )
    participants = client.get("/activities").json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": expected_message}
    assert email in participants


def test_signup_rejects_duplicate_registration_without_changing_participants(client):
    # Arrange
    email = "michael@mergington.edu"
    endpoint = "/activities/Chess%20Club/signup"
    participants_before_duplicate = client.get("/activities").json()["Chess Club"]["participants"]

    # Act
    duplicate_response = client.post(endpoint, params={"email": email})
    participants_after_duplicate = client.get("/activities").json()["Chess Club"]["participants"]

    # Assert
    assert duplicate_response.status_code == 400
    assert duplicate_response.json() == {
        "detail": "Student already signed up for this activity"
    }
    assert participants_after_duplicate == participants_before_duplicate


def test_signup_returns_not_found_for_unknown_activity(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.post(
        "/activities/Unknown%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_requires_email(client):
    # Arrange
    endpoint = "/activities/Chess%20Club/signup"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 422


def test_delete_signup_unregisters_participant(client):
    # Arrange
    email = "michael@mergington.edu"
    expected_message = f"Unregistered {email} from Chess Club"

    # Act
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )
    participants = client.get("/activities").json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": expected_message}
    assert email not in participants


def test_delete_signup_returns_not_found_for_unknown_activity(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Unknown%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_delete_signup_returns_not_found_for_unregistered_participant(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student is not signed up for this activity"
    }
