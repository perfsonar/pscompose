import requests
from playwright.sync_api import Page, expect, sync_playwright

BASE_URL = "http://localhost:5001"
API_BASE = "http://localhost:8000/api"

# ── Fixture helpers ────────────────────────────────────────────────────────────


def _create(datatype: str, payload: dict) -> str:
    r = requests.post(f"{API_BASE}/{datatype}/", json=payload)
    r.raise_for_status()
    return r.json()["id"]


def _delete(datatype: str, item_id: str) -> None:
    requests.delete(f"{API_BASE}/{datatype}/{item_id}/")


def create_address() -> str:
    return _create(
        "address",
        {
            "ref_set": [],
            "type": "address",
            "json": {"address": "10.0.0.1", "no-agent": False, "disabled": False},
            "name": "pw-test-address",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )


def create_group(address_id: str) -> str:
    return _create(
        "group",
        {
            "ref_set": [],
            "type": "group",
            "group_type": "list",
            "json": {
                "type": "list",
                "addresses": [address_id],
            },
            "name": "pw-test-group",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )


def create_schedule() -> str:
    return _create(
        "schedule",
        {
            "ref_set": [],
            "type": "schedule",
            "json": {"repeat": "PT4H"},
            "name": "pw-test-schedule",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )


def create_test() -> str:
    return _create(
        "test",
        {
            "ref_set": [],
            "type": "test",
            "json": {"duration": "PT10S", "schema": 2, "type": "idle", "version": "2"},
            "name": "pw-test-test",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )


def create_task(group_id: str, test_id: str) -> str:
    return _create(
        "task",
        {
            "ref_set": [],
            "type": "task",
            "json": {"disabled": False, "group": group_id, "test": test_id},
            "name": "pw-task-task",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )


# ── Shared assertions ──────────────────────────────────────────────────────────


def assert_edit_form_structure(page: Page, item_name: str) -> None:
    """Checks that the read/edit form wrapper is visible with all key elements."""
    wrapper = page.locator(".datatype.edit-form")
    expect(wrapper).to_be_visible(timeout=15_000)

    # Item name heading (set after json-form mounts)
    heading = wrapper.locator("#data-name")
    expect(heading).to_be_visible(timeout=10_000)
    expect(heading).to_have_text(item_name)

    # Edit pencil icon
    edit_icon = wrapper.locator("#edit-icon")
    expect(edit_icon).to_be_visible()

    # JSON form in read-only state
    json_form = wrapper.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)
    expect(json_form).to_have_attribute("readonly", "true")


def assert_edit_mode(page: Page) -> None:
    """After clicking the edit icon, json-form should become editable."""
    wrapper = page.locator(".datatype.edit-form")
    json_form = wrapper.locator("json-form")

    edit_icon = wrapper.locator("#edit-icon")
    edit_icon.click()
    page.wait_for_timeout(300)

    expect(json_form).to_have_attribute("readonly", "false")

    # Action buttons
    expect(wrapper.locator("#delete-btn")).to_be_visible()
    expect(wrapper.locator("#save-btn")).to_be_visible()
    expect(wrapper.locator("#cancel-btn")).to_be_visible()
    assert "edit=true" in page.url


def assert_cancel_returns_to_readonly(page: Page) -> None:
    """Clicking Cancel from edit mode returns the form to read-only state."""
    wrapper = page.locator(".datatype.edit-form")
    json_form = wrapper.locator("json-form")

    cancel_btn = wrapper.locator("#cancel-btn")
    cancel_btn.click()
    page.wait_for_timeout(300)

    expect(json_form).to_have_attribute("readonly", "true")
    assert "edit=true" not in page.url


# ── Per-datatype test functions ────────────────────────────────────────────────


def edit_form_address(page: Page) -> None:
    item_id = create_address()
    try:
        page.goto(f"{BASE_URL}/address/?id={item_id}")
        assert_edit_form_structure(page, "pw-test-address")

        # Address-specific: "Template using this address" action icon present
        addr_btn = page.locator("#address-template-btn")
        expect(addr_btn).to_be_visible()

        assert_edit_mode(page)
        assert_cancel_returns_to_readonly(page)

        # References section
        refset = page.locator(".refset")
        expect(refset).to_be_visible()
        expect(refset.locator(".refset-name")).to_have_text("References")
    finally:
        _delete("address", item_id)


def edit_form_group(page: Page) -> None:
    addr_id = create_address()
    grp_id = create_group(addr_id)
    try:
        page.goto(f"{BASE_URL}/group/?id={grp_id}")
        assert_edit_form_structure(page, "pw-test-group")
        assert_edit_mode(page)
        assert_cancel_returns_to_readonly(page)
    finally:
        _delete("group", grp_id)
        _delete("address", addr_id)


def edit_form_schedule(page: Page) -> None:
    item_id = create_schedule()
    try:
        page.goto(f"{BASE_URL}/schedule/?id={item_id}")
        assert_edit_form_structure(page, "pw-test-schedule")
        assert_edit_mode(page)
        assert_cancel_returns_to_readonly(page)
    finally:
        _delete("schedule", item_id)


def edit_form_test(page: Page) -> None:
    item_id = create_test()
    try:
        page.goto(f"{BASE_URL}/test/?id={item_id}")
        assert_edit_form_structure(page, "pw-test-test")
        assert_edit_mode(page)
        assert_cancel_returns_to_readonly(page)
    finally:
        _delete("test", item_id)


def edit_form_delete_modal(page: Page) -> None:
    """Clicking the Delete button opens the delete confirmation modal."""
    item_id = create_address()
    try:
        page.goto(f"{BASE_URL}/address/?id={item_id}")

        wrapper = page.locator(".datatype.edit-form")
        expect(wrapper).to_be_visible(timeout=15_000)

        # Switch to edit mode so delete is actionable
        wrapper.locator("#edit-icon").click()
        page.wait_for_timeout(300)

        delete_btn = wrapper.locator("#delete-btn")
        expect(delete_btn).to_be_visible()
        expect(delete_btn).to_be_enabled()
        delete_btn.click()

        # ps-modal opens by setting style.display = "block"
        delete_modal = page.locator("#delete-modal")
        expect(delete_modal).to_have_css("display", "block", timeout=5_000)

        # Close the modal by clicking the Cancel button (#confirm-no)
        no_btn = delete_modal.locator("#confirm-no")
        expect(no_btn).to_be_visible()
        no_btn.click()

        # Confirm modal is closed (display returns to none/empty)
        expect(delete_modal).not_to_have_css("display", "block", timeout=5_000)

    finally:
        _delete("address", item_id)


def edit_form_template_action_icons(page: Page) -> None:
    """Template edit form exposes Download, Copy, and Open JSON action icons."""
    addr_id = create_address()
    grp_id = create_group(addr_id)
    test_id = create_test()
    task_id = create_task(grp_id, test_id)
    item_id = _create(
        "template",
        {
            "ref_set": [],
            "type": "template",
            "json": {"tasks": [task_id]},
            "name": "pw-template-template",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )
    try:
        page.goto(f"{BASE_URL}/template/?id={item_id}")

        wrapper = page.locator(".datatype.edit-form")
        expect(wrapper).to_be_visible(timeout=15_000)

        # Template-specific icons become visible in read mode
        expect(wrapper.locator("#export-json-btn")).to_be_visible(timeout=5_000)
        expect(wrapper.locator("#copy-json-btn")).to_be_visible()
        expect(wrapper.locator("#url-json-btn")).to_be_visible()
    finally:
        _delete("template", item_id)
        _delete("task", task_id)
        _delete("test", test_id)
        _delete("group", grp_id)
        _delete("address", addr_id)


def edit_form_favorite_star(page: Page) -> None:
    """Favorite star checkbox is present in the edit form header."""
    item_id = create_address()
    try:
        page.goto(f"{BASE_URL}/address/?id={item_id}")

        wrapper = page.locator(".datatype.edit-form")
        expect(wrapper).to_be_visible(timeout=15_000)

        star = wrapper.locator(".header ps-input-checkbox-star")
        expect(star).to_be_visible(timeout=10_000)
    finally:
        _delete("address", item_id)


# ── Entry point ────────────────────────────────────────────────────────────────


def test_edit_forms():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        edit_form_address(page)
        edit_form_group(page)
        edit_form_schedule(page)
        edit_form_test(page)
        edit_form_delete_modal(page)
        edit_form_template_action_icons(page)
        edit_form_favorite_star(page)

        context.close()
        browser.close()
