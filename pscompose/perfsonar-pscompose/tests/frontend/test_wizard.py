from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5001"

# Wizard order matches psCompose.metadata.wizard.order in app/index.html
WIZARD_STEPS = [
    {"step": 1, "key": "address", "singular": "Address", "url": "/wizard/1/address/"},
    {"step": 2, "key": "group", "singular": "Group", "url": "/wizard/2/group/"},
    {"step": 3, "key": "archive", "singular": "Archive", "url": "/wizard/3/archive/"},
    {"step": 4, "key": "schedule", "singular": "Schedule", "url": "/wizard/4/schedule/"},
    {"step": 5, "key": "test", "singular": "Test", "url": "/wizard/5/test/"},
    {"step": 6, "key": "task", "singular": "Task", "url": "/wizard/6/task/"},
    {"step": 7, "key": "template", "singular": "Template", "url": "/wizard/7/template/"},
]


# ── Per-step structure ─────────────────────────────────────────────────────────


def wizard_step_structure(page: Page, step: dict) -> None:
    """Each wizard step renders the page wrapper, header, and step section."""
    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    # Header
    header = wizard_page.locator(".wizard-header")
    expect(header).to_be_visible()

    # Prev button
    prev_btn = header.locator("#prev-btn")
    expect(prev_btn).to_be_visible()

    # Progress bar section
    progress_section = header.locator(".ps-progress-bar")
    expect(progress_section).to_be_visible()
    expect(progress_section.locator("h3")).to_have_text("New Template")
    expect(progress_section.locator("ps-progress-bar")).to_be_visible()

    # Next button
    next_btn = header.locator("#next-btn")
    expect(next_btn).to_be_visible()

    # Step section
    step_section = wizard_page.locator(".step-section")
    expect(step_section).to_be_visible()

    step_heading = step_section.locator("h2").first
    expect(step_heading).to_be_visible()
    expect(step_heading).to_have_text(f"Step {step['step']}) {step['singular']}")


def wizard_step_prev_next_labels(page: Page, step: dict) -> None:
    """Prev/Next button labels depend on step position."""
    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    prev_btn = wizard_page.locator("#prev-btn")
    next_btn = wizard_page.locator("#next-btn")

    expected_prev = "Cancel" if step["step"] == 1 else "Previous"
    expect(prev_btn).to_have_attribute("label", expected_prev)

    expect(next_btn).to_have_attribute("label", "Next")


def wizard_step_dropdown_and_new_button(page: Page, step: dict) -> None:
    """Steps 1-6 show a ps-select dropdown and a 'New {singular}' button."""
    if step["step"] == 7:
        return  # Step 7 renders a form instead

    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    step_box = wizard_page.locator(".step-box")
    expect(step_box).to_be_visible()

    # Dropdown
    dropdown = step_box.locator("ps-select")
    expect(dropdown).to_be_visible()
    expect(dropdown).to_have_attribute("label", step["singular"])

    # "New {singular}" button
    new_btn = step_box.locator("#new-btn")
    expect(new_btn).to_be_visible()
    expect(new_btn).to_have_attribute("label", f"New {step['singular']}")


def wizard_step_prev_navigates(page: Page, step: dict) -> None:
    """Clicking Prev on steps > 1 navigates to the previous step."""
    if step["step"] == 1:
        return  # Step 1 Prev goes to home, tested separately

    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    prev_btn = wizard_page.locator("#prev-btn")
    prev_btn.click()

    prev_step = WIZARD_STEPS[step["step"] - 2]
    page.wait_for_url(f"**{prev_step['url']}**", timeout=5_000)
    assert prev_step["url"] in page.url


def wizard_step1_cancel_navigates_home(page: Page) -> None:
    """On step 1, the Prev/Cancel button goes back to the homepage."""
    page.goto(f"{BASE_URL}/wizard/1/address/")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    prev_btn = wizard_page.locator("#prev-btn")
    expect(prev_btn).to_have_attribute("label", "Cancel")
    prev_btn.click()

    page.wait_for_url(f"{BASE_URL}/", timeout=5_000)
    assert page.url == f"{BASE_URL}/"


def wizard_step_next_navigates(page: Page, step: dict) -> None:
    """Clicking Next on steps 1-5 navigates to the following step."""
    if step["step"] >= 6:
        return  # Steps 6 and 7 need form interaction to proceed

    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    next_btn = wizard_page.locator("#next-btn")
    next_btn.click()

    next_step = WIZARD_STEPS[step["step"]]  # index is step number (0-based)
    page.wait_for_url(f"**{next_step['url']}**", timeout=5_000)
    assert next_step["url"] in page.url


# ── Step 7: template form ──────────────────────────────────────────────────────


def wizard_step7_renders_new_form(page: Page) -> None:
    """Step 7 replaces the dropdown with the template new form."""
    page.goto(f"{BASE_URL}/wizard/7/template/")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    # Step box becomes step-box-column with data_new_form partial
    step_box = wizard_page.locator(".step-box-column")
    expect(step_box).to_be_visible(timeout=10_000)

    new_form = step_box.locator("#data-new-form")
    expect(new_form).to_be_visible(timeout=10_000)

    json_form = new_form.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)

    # Next button triggers save-modal (label stays "Next"; link is removed)
    next_btn = wizard_page.locator("#next-btn")
    expect(next_btn).to_have_attribute("label", "Next")
    expect(next_btn).to_have_attribute("confirm-modal", "save-modal")


# ── Complete page ──────────────────────────────────────────────────────────────


def wizard_complete_page_no_nav_buttons(page: Page) -> None:
    """After save success on step 7, the complete page shows no wizard nav buttons."""
    # This page normally requires an id param; test with a dummy to see the read form
    # Without a real id the page would redirect to wizard/7/template/ — skip with note
    # Test is included as documentation of expected behavior when ?id is provided.
    pass


def wizard_no_left_subnav(page: Page, step: dict) -> None:
    """The left subnav stays closed during wizard steps."""
    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    subnav_container = page.locator(".subnav-container")
    expect(subnav_container).not_to_have_class("open")


# ── New-item inline form in wizard steps ──────────────────────────────────────


def wizard_new_button_loads_inline_form(page: Page, step: dict) -> None:
    """Clicking 'New {singular}' in a wizard step loads the new form inline."""
    if step["step"] == 7:
        return

    page.goto(f"{BASE_URL}{step['url']}")
    page.wait_for_load_state("networkidle")

    wizard_page = page.locator(".wizard-page")
    expect(wizard_page).to_be_visible(timeout=10_000)

    new_btn = wizard_page.locator("#new-btn")
    expect(new_btn).to_be_visible()
    new_btn.click()
    page.wait_for_timeout(500)

    # URL should include ?new=true
    assert "new=true" in page.url

    # Inline new form loads on the right panel
    new_form = page.locator("#data-new-form")
    expect(new_form).to_be_visible(timeout=10_000)


# ── Entry point ────────────────────────────────────────────────────────────────


def test_wizard(page: Page) -> None:
    # Structure checks for every step
    for step in WIZARD_STEPS:
        wizard_step_structure(page, step)
        wizard_step_prev_next_labels(page, step)
        wizard_step_dropdown_and_new_button(page, step)
        wizard_no_left_subnav(page, step)

    # Navigation checks
    wizard_step1_cancel_navigates_home(page)
    for step in WIZARD_STEPS:
        wizard_step_prev_navigates(page, step)
        wizard_step_next_navigates(page, step)

    # Inline new-item form
    for step in WIZARD_STEPS:
        wizard_new_button_loads_inline_form(page, step)

    # Step 7 template form
    wizard_step7_renders_new_form(page)
