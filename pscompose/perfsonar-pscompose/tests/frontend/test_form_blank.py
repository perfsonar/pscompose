import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5001"

DATATYPES = [
    {"key": "address", "article": "an", "singular": "Address", "plural": "Addresses"},
    {"key": "archive", "article": "an", "singular": "Archive", "plural": "Archives"},
    {"key": "context", "article": "a", "singular": "Context", "plural": "Contexts"},
    {"key": "group", "article": "a", "singular": "Group", "plural": "Groups"},
    {"key": "schedule", "article": "a", "singular": "Schedule", "plural": "Schedules"},
    {"key": "task", "article": "a", "singular": "Task", "plural": "Tasks"},
    {"key": "template", "article": "a", "singular": "Template", "plural": "Templates"},
    {"key": "test", "article": "a", "singular": "Test", "plural": "Tests"},
]


def blank_form_heading(page: Page, dt: dict) -> None:
    """Blank form shows 'Select a/an {type} to continue.' when no item selected."""
    page.goto(f"{BASE_URL}/{dt['key']}/")

    blank_form = page.locator(".datatype.error-form")
    expect(blank_form).to_be_visible(timeout=10_000)

    heading = blank_form.locator("h4")
    expect(heading).to_be_visible()
    expect(heading).to_have_text(f"Select {dt['article']} {dt['key']} to continue.")


def blank_form_subnav_opens(page: Page, dt: dict) -> None:
    """Navigating to a datatype list page auto-opens the subnav panel."""
    page.goto(f"{BASE_URL}/{dt['key']}/")
    page.wait_for_load_state("networkidle")

    subnav_container = page.locator(".subnav-container")
    expect(subnav_container).to_be_visible(timeout=10_000)
    expect(subnav_container).to_have_class(re.compile(r"open"))

    subnav = subnav_container.locator(".subnav")
    expect(subnav).to_be_visible()

    # Subnav heading shows plural name
    header_h1 = subnav.locator("h1")
    expect(header_h1).to_be_visible()
    expect(header_h1).to_have_text(dt["plural"])

    # Search input
    search = subnav.locator("#subnav-search")
    expect(search).to_be_visible()
    expect(search).to_have_attribute("placeholder", f"Search {dt['singular']}")

    # "New" button
    new_btn = subnav.locator("ps-button[label='New']")
    expect(new_btn).to_be_visible()
    expect(new_btn).to_have_attribute("link", f"/{dt['key']}/new/")


def blank_form_subnav_new_button_navigates(page: Page, dt: dict) -> None:
    """Clicking the subnav 'New' button navigates to the new form page."""
    page.goto(f"{BASE_URL}/{dt['key']}/")
    page.wait_for_load_state("networkidle")

    subnav = page.locator(".subnav")
    expect(subnav).to_be_visible(timeout=10_000)

    new_btn = subnav.locator("ps-button[label='New']")
    expect(new_btn).to_be_visible()
    new_btn.click()

    page.wait_for_url(f"**/{dt['key']}/new/**", timeout=5_000)
    assert f"/{dt['key']}/new/" in page.url


def blank_form_subnav_search_filters(page: Page, dt: dict) -> None:
    """Typing in subnav search input filters the visible list items."""
    page.goto(f"{BASE_URL}/{dt['key']}/")
    page.wait_for_load_state("networkidle")

    subnav = page.locator(".subnav")
    expect(subnav).to_be_visible(timeout=10_000)

    search = subnav.locator("#subnav-search")
    expect(search).to_be_visible()

    # Type a search term unlikely to match any item
    search.fill("zzz_playwright_no_match_zzz")
    page.wait_for_timeout(300)

    items = subnav.locator("#subnav-list li.subnav-item")
    count = items.count()
    for i in range(count):
        expect(items.nth(i)).to_have_css("display", "none")

    # Clear search — items reappear
    search.fill("")
    page.wait_for_timeout(300)
    for i in range(count):
        expect(items.nth(i)).not_to_have_css("display", "none")


def blank_form_subnav_item_click_loads_edit(page: Page, dt: dict) -> None:
    """Clicking a subnav item while on the blank form loads the edit/read form."""
    page.goto(f"{BASE_URL}/{dt['key']}/")
    page.wait_for_load_state("networkidle")

    subnav = page.locator(".subnav")
    expect(subnav).to_be_visible(timeout=10_000)

    items = subnav.locator("#subnav-list li.subnav-item")
    if items.count() == 0:
        return  # No items to click — skip

    first_item = items.nth(0)
    expect(first_item).to_be_visible()
    first_item.click()

    # URL should include ?id=
    page.wait_for_url(re.compile(r"\?id="), timeout=5_000)
    assert "id=" in page.url

    # Edit form should be visible
    edit_form = page.locator(".datatype.edit-form")
    expect(edit_form).to_be_visible(timeout=10_000)


@pytest.mark.parametrize("dt", DATATYPES, ids=[d["key"] for d in DATATYPES])
def test_blank_form(page: Page, dt: dict) -> None:
    blank_form_heading(page, dt)
    blank_form_subnav_opens(page, dt)
    blank_form_subnav_search_filters(page, dt)
    blank_form_subnav_new_button_navigates(page, dt)
    blank_form_subnav_item_click_loads_edit(page, dt)
