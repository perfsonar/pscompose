from playwright.sync_api import Page, expect
import pytest

BASE_URL = "http://localhost:5001"
DATATYPES = [
    {"key": "address", "singular": "Address"},
    {"key": "archive", "singular": "Archive"},
    {"key": "context", "singular": "Context"},
    {"key": "group", "singular": "Group"},
    {"key": "schedule", "singular": "Schedule"},
    {"key": "task", "singular": "Task"},
    {"key": "template", "singular": "Template"},
    {"key": "test", "singular": "Test"},
]


def new_form_structure(page: Page, dt: dict) -> None:
    """New form renders the wrapper, heading, json-form, and save button."""
    page.goto(f"{BASE_URL}/{dt['key']}/new/")

    wrapper = page.locator(".datatype.new-form")
    expect(wrapper).to_be_visible(timeout=10_000)

    # JSON Forms element
    form = wrapper.locator("#data-new-form")
    expect(form).to_be_visible()

    json_form = form.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)

    # Heading set by JS after json-form mounts
    heading = wrapper.locator("#data-name")
    expect(heading).to_be_visible(timeout=10_000)
    expect(heading).to_have_text(f"New {dt['singular']}")

    # Save button
    save_btn = form.locator("ps-button[type='submit'][label='Save']")
    expect(save_btn).to_be_visible()


def new_form_save_button_attributes(page: Page, dt: dict) -> None:
    """Save button has the correct confirm-modal and theme attributes."""
    page.goto(f"{BASE_URL}/{dt['key']}/new/")

    wrapper = page.locator(".datatype.new-form")
    expect(wrapper).to_be_visible(timeout=10_000)

    save_btn = page.locator("#data-new-form ps-button[type='submit']")
    expect(save_btn).to_be_visible(timeout=10_000)
    expect(save_btn).to_have_attribute("confirm-modal", "save-modal")
    expect(save_btn).to_have_attribute("theme", "Secondary")
    expect(save_btn).to_have_attribute("righticon", "save")


def new_form_empty_submit_stays_on_page(page: Page, dt: dict) -> None:
    """Submitting an empty new form stays on the page (validation prevents save)."""
    page.goto(f"{BASE_URL}/{dt['key']}/new/")

    wrapper = page.locator(".datatype.new-form")
    expect(wrapper).to_be_visible(timeout=10_000)

    # Wait for json-form to mount before clicking save
    json_form = page.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)

    save_btn = page.locator("ps-button[type='submit'][label='Save']")
    expect(save_btn).to_be_visible()
    save_btn.click()
    page.wait_for_timeout(500)

    # Still on the new form page
    assert f"/{dt['key']}/new/" in page.url

    # Save modal should not have opened (form failed validation)
    save_modal = page.locator("#save-modal")
    expect(save_modal).not_to_have_attribute("open", "")


def new_form_subnav_closed(page: Page, dt: dict) -> None:
    """Subnav panel is closed on the new form page."""
    page.goto(f"{BASE_URL}/{dt['key']}/new/")
    page.wait_for_load_state("networkidle")

    subnav_container = page.locator(".subnav-container")
    # Subnav should NOT have the 'open' class on a new form page
    expect(subnav_container).not_to_have_class("open")


def new_form_star_checkbox_present(page: Page, dt: dict) -> None:
    """Favorite star checkbox is present in the new form header."""
    page.goto(f"{BASE_URL}/{dt['key']}/new/")

    wrapper = page.locator(".datatype.new-form")
    expect(wrapper).to_be_visible(timeout=10_000)

    star = wrapper.locator(".header ps-input-checkbox-star")
    expect(star).to_be_visible(timeout=10_000)


def new_form_nav_top_visible(page: Page) -> None:
    """Top navigation bar is visible on new form pages."""
    page.goto(f"{BASE_URL}/address/new/")

    nav_top = page.get_by_role("navigation", name="Top Navigation")
    expect(nav_top).to_be_visible()

    logo = nav_top.get_by_role("link", name="Go to homepage")
    expect(logo).to_be_visible()


@pytest.mark.parametrize("dt", DATATYPES, ids=[d["key"] for d in DATATYPES])
def test_blank_form(page: Page, dt: dict) -> None:
    new_form_nav_top_visible(page)
    new_form_structure(page, dt)
    new_form_save_button_attributes(page, dt)
    new_form_empty_submit_stays_on_page(page, dt)
    new_form_subnav_closed(page, dt)
    new_form_star_checkbox_present(page, dt)
