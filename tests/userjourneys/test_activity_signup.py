from uuid import uuid4

from playwright.sync_api import Page, expect


def test_student_can_sign_up_for_multiple_activities(page: Page, live_app: str):
    email = f"journey-{uuid4().hex}@mergington.edu"
    activities = ("Chess Club", "Art Club")

    page.goto(live_app)

    for activity in activities:
        expect(page.get_by_role("heading", name=activity, exact=True)).to_be_visible()
        page.get_by_label("Student Email:").fill(email)
        page.get_by_label("Select Activity:").select_option(label=activity)
        page.get_by_role("button", name="Sign Up").click()

        expect(page.get_by_role("status")).to_have_text(
            f"Signed up {email} for {activity}"
        )

    for activity in activities:
        activity_card = page.locator(".activity-card").filter(
            has=page.get_by_role("heading", name=activity, exact=True)
        )
        expect(
            activity_card.locator(".participant-email").filter(has_text=email)
        ).to_be_visible()
