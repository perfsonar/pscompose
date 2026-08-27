from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5001"


def test_homepage_getting_started_heading(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    homepage = page.get_by_role("main", name="psCompose Homepage")
    expect(homepage).to_be_visible()

    # Check for Getting Started banner
    banner = homepage.get_by_role("banner")
    expect(banner).to_be_visible()
    expect(banner).to_have_attribute("aria-labelledby", "getting-started-heading")

    banner_heading = homepage.locator("#getting-started-heading")
    expect(banner_heading).to_be_visible()
    expect(banner_heading).to_have_text("Getting Started")

    welcome_text = homepage.locator("#welcome-text")
    expect(welcome_text).to_be_visible()
    expect(welcome_text).to_contain_text("Welcome to pSCompose!")
    expect(welcome_text).to_contain_text(
        "Are you starting a template from scratch? Start by entering hosts."
    )
    expect(welcome_text).to_contain_text("Do you need to import an existing template?")

    # Check for Getting Started Options
    option_list = homepage.get_by_role("list", name="Template creation options")
    expect(option_list).to_be_visible()
    expect(option_list).to_have_class("getting-started-boxes")

    list_items = option_list.get_by_role("listitem")
    expect(list_items).to_have_count(2)

    # Import Template box
    first_item = list_items.nth(0)
    expect(first_item).to_be_visible()
    expect(first_item).to_have_class("list-box")
    expect(first_item.get_by_role("heading", level=4, name="Import Template")).to_be_visible()
    import_button = first_item.locator('ps-button[aria-label="Import an existing template"]')
    expect(import_button).to_be_visible()
    expect(import_button).to_have_attribute("aria-label", "Import an existing template")
    first_p = first_item.locator("p.box-text")
    expect(first_p).to_contain_text("import an existing template")
    expect(first_p).to_contain_text("after import")

    # Wizard box
    second_item = list_items.nth(1)
    expect(second_item).to_be_visible()
    expect(second_item).to_have_class("list-box")
    expect(second_item.get_by_role("heading", level=4, name="Create New Template")).to_be_visible()
    create_button = second_item.locator(
        'ps-button[aria-label="Create a new template from scratch"]'
    )
    expect(create_button).to_be_visible()
    expect(create_button).to_have_attribute("aria-label", "Create a new template from scratch")
    second_p = second_item.locator("p.box-text")
    expect(second_p).to_contain_text("from scratch")

    # Button interactions
    import_button.click()
    assert "/import/" in page.url
    page.go_back()

    create_button.click()
    assert "wizard/1/address" in page.url
    page.go_back()

    # Responsive checks - example small viewport
    page.set_viewport_size({"width": 375, "height": 667})
    expect(homepage).to_be_visible()
    expect(import_button).to_be_visible()
    expect(create_button).to_be_visible()


def test_homepage_published_templates(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    homepage = page.get_by_role("main", name="psCompose Homepage")
    expect(homepage).to_be_visible()

    # Check for Published Templates section
    published_section = homepage.locator('section[aria-labelledby="published-templates-heading"]')
    expect(published_section).to_be_visible()
    expect(published_section).to_have_attribute("aria-labelledby", "published-templates-heading")

    section_heading = published_section.get_by_role("heading", level=4, name="Published Templates")
    expect(section_heading).to_be_visible()

    # Check for Published Templates table
    templates_table = published_section.get_by_role("table", name="Published Templates Table")
    expect(templates_table).to_be_visible()

    # Check table content — wait for HTMX/nunjucks to populate the tbody
    table_rows = templates_table.locator("tbody tr")
    expect(table_rows.first).to_be_visible()
    row_count = table_rows.count()

    if row_count == 1:
        cell = table_rows.nth(0).locator("td")
        expect(cell).to_have_attribute("colspan", "3")
        expect(cell).to_contain_text("No published templates")
        expect(cell).to_have_css("text-align", "center")
    else:
        count = table_rows.count()
        for i in range(count):
            row = table_rows.nth(i)
            cells = row.locator("td")

            expect(cells).to_have_count(3)
            # TODO: Further check table content once templates works


def test_homepage_nav_top(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    nav_top = page.get_by_role("navigation", name="Top Navigation")
    expect(nav_top).to_be_visible()

    # Check for Logo and Site Name
    logo = nav_top.get_by_role("link", name="Go to homepage")
    expect(logo).to_be_visible()
    expect(logo.get_by_alt_text("Perfsonar Icon")).to_be_visible()
    expect(logo.get_by_text("pSCompose")).to_be_visible()

    # Check for README link
    readme_link = nav_top.get_by_role("link", name="README")
    expect(readme_link).to_be_visible()
    expect(readme_link).to_have_attribute("href", "https://docs.perfsonar.net/index.html")
    expect(readme_link).to_have_class("readme")

    # Check for User Account button (ps-button; aria-label lives on the element itself)
    user_button = nav_top.locator('ps-button[aria-label="User account"]')
    expect(user_button).to_be_visible()
    expect(user_button).to_have_attribute("aria-label", "User account")

    # Button interactions
    logo.click()
    assert page.url == "http://localhost:5001/"

    # readme_link.click()
    # assert page.url == 'https://docs.perfsonar.net/index.html'
    # page.go_back()

    # user_button.click()
    # assert page.url.endswith("/account/")
    # page.go_back()


def test_homepage_nav_left(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    nav_left = page.get_by_role("navigation", name="Menu Navigation")
    expect(nav_left).to_be_visible()

    menu = nav_left.get_by_role("menu", name="Primary menu")
    expect(menu).to_be_visible()
    expect(menu).to_have_attribute("aria-orientation", "vertical")
    menu_items = menu.get_by_role("menuitem")

    expect(menu_items).to_have_count(8)

    # nav keys are singular; order matches psCompose.nav definition in app/index.html
    expected_nav = [
        ("template", "Templates"),
        ("task", "Tasks"),
        ("test", "Tests"),
        ("schedule", "Schedules"),
        ("archive", "Archives"),
        ("group", "Groups"),
        ("context", "Contexts"),
        ("address", "Addresses"),
    ]

    for idx, (menu_id, menu_label) in enumerate(expected_nav):
        item = menu_items.nth(idx)
        expect(item).to_have_attribute("id", menu_id)
        expect(item).to_have_attribute("data-subnav", menu_id)
        expect(item).to_have_attribute("aria-haspopup", "true")
        expect(item).to_have_attribute("aria-expanded", "false")
        expect(item).to_have_attribute("aria-controls", f"subnav-content-{menu_id}")

        # Icon is decorative
        icon = item.locator('svg[aria-hidden="true"]')
        expect(icon).to_be_visible()

        # Label text (plural from nav config)
        label = item.locator("p")
        expect(label).to_be_visible()
        expect(label).to_have_text(menu_label)

        # Interactions
        item.click()
        subnav_container = nav_left.locator("div.subnav-container")
        expect(subnav_container).to_be_visible()

        # Subnav content (rendered inside subnav-container by JS)
        subnav = subnav_container.locator(".subnav")
        expect(subnav).to_be_visible()

        expect(subnav.locator("h1")).to_be_visible()
        expect(subnav.locator('ps-button[theme="AddBtn"]')).to_be_visible()

        # Check subnav search input presence and placeholder
        search_input = subnav.locator("#subnav-search")
        expect(search_input).to_be_visible()
        placeholder = search_input.get_attribute("placeholder")
        assert "Search" in placeholder

        # Check subnav list items
        subnav_list = subnav.locator("#subnav-list")
        subnav_items = subnav_list.locator("li.subnav-item")
        count = subnav_items.count()

        if count > 0:
            # Check all items' structure before navigating
            for i in range(count):
                data_item = subnav_items.nth(i)
                expect(data_item).to_be_visible()
                expect(data_item).to_have_class("subnav-item")
                expect(data_item.locator('.item-info svg[aria-hidden="true"]')).to_be_visible()
                expect(data_item.locator("h5")).to_be_visible()

            # Click first item to verify navigation, then go back
            subnav_items.nth(0).click()
            assert menu_id in page.url
            page.go_back()
            # go_back() reloads the page so the subnav is already closed
        else:
            item.click()  # Close subnav (only needed when no navigation occurred)


def test_homepage_nav_shortcuts(page: Page) -> None:
    page.goto(f"{BASE_URL}/")
    nav_left = page.get_by_role("navigation", name="Menu Navigation")
    expect(nav_left).to_be_visible()
