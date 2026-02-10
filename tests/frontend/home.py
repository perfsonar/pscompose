from playwright.sync_api import Playwright, Page, expect, sync_playwright

def homepage_getting_started_heading(p: Page) -> None:
    homepage = p.get_by_role("main", name="psCompose Homepage")
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
    expect(welcome_text).to_contain_text("Are you starting a template from scratch? Start by entering hosts.")
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
    import_button = first_item.get_by_role("button", name="Import an existing template")
    expect(import_button).to_be_visible()
    expect(import_button).to_have_attribute("aria-label", "Import an existing template")
    first_p = first_item.locator("p.box-text")
    expect(first_p).to_contain_text("uploading the file")
    expect(first_p).to_contain_text("once imported")

    # Wizard box
    second_item = list_items.nth(1)
    expect(second_item).to_be_visible()
    expect(second_item).to_have_class("list-box")
    expect(second_item.get_by_role("heading", level=4, name="Create New Template")).to_be_visible()
    create_button = second_item.get_by_role("button", name="Create a new template from scratch")
    expect(create_button).to_be_visible()
    expect(create_button).to_have_attribute("aria-label", "Create a new template from scratch")
    second_p = second_item.locator("p.box-text")
    expect(second_p).to_contain_text("walk you through")
    expect(second_p).to_contain_text("from scratch")

    # Button interactions
    import_button.click()
    assert "/import/1/import_template/" in p.url
    p.go_back()

    create_button.click()
    assert "/wizard/1/addresses/" in p.url
    p.go_back()

    # Responsive checks - example small viewport
    p.set_viewport_size({"width": 375, "height": 667})
    expect(homepage).to_be_visible()
    expect(import_button).to_be_visible()
    expect(create_button).to_be_visible()

def homepage_published_templates(p: Page) -> None:
    homepage = p.get_by_role("main", name="psCompose Homepage")
    expect(homepage).to_be_visible()

    # Check for Published Templates section
    published_section = homepage.locator('section[aria-labelledby="published-templates-heading"]')
    expect(published_section).to_be_visible()
    expect(published_section).to_have_attribute("aria-labelledby", "published-templates-heading")

    section_heading = published_section.get_by_role("heading", level=3, name="Published Templates")
    expect(section_heading).to_be_visible()

    # Check for Published Templates table
    templates_table = published_section.get_by_role("table", name="Published Templates Table")
    expect(templates_table).to_be_visible()
    
    # Check table content
    table_rows = templates_table.locator("tbody tr")

    row_count = table_rows.count()
    assert row_count >= 1, f"Expected at least 1 row, got {row_count}"

    if row_count == 1:
        cell = table_rows.nth(0).locator('td')
        expect(cell).to_have_attribute('colspan', '6')
        expect(cell).to_contain_text('No published templates')
        expect(cell).to_have_css('text-align', 'center')
    else:
        count = table_rows.count()
        for i in range(count):
            row = table_rows.nth(i)
            cells = row.locator('td')
            
            expect(cells).to_have_count(6)
            # TODO: Further check table content once templates works

def homepage_nav_top(p: Page) -> None:
    nav_top = p.get_by_role("navigation", name="Top Navigation")
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

    # Check for User Account button
    user_button = nav_top.get_by_role("button", name="User account")
    expect(user_button).to_be_visible()
    expect(user_button).to_have_attribute("aria-label", "User account")

    # Button interactions
    logo.click()
    assert p.url == 'http://localhost:5001/'

    # readme_link.click()
    # assert p.url == 'https://docs.perfsonar.net/index.html'
    # p.go_back()

    # user_button.click()
    # assert p.url.endswith("/account/")
    # p.go_back()

def homepage_nav_left(p: Page) -> None:
    nav_left = p.get_by_role("navigation", name="Menu Navigation")
    expect(nav_left).to_be_visible()

    menu = nav_left.get_by_role("menu", name="Primary menu")
    expect(menu).to_be_visible()
    expect(menu).to_have_attribute("aria-orientation", "vertical")
    menu_items = menu.get_by_role("menuitem")

    expect(menu_items).to_have_count(8)

    expected_ids = [
        "templates",
        "tasks",
        "contexts",
        "tests",
        "archives",
        "schedules",
        "groups",
        "addresses",
    ]

    for idx, menu_id in enumerate(expected_ids):
        item = menu_items.nth(idx)
        expect(item).to_have_attribute("id", menu_id)
        expect(item).to_have_attribute("data-submenu", menu_id)
        expect(item).to_have_attribute("aria-haspopup", "true")
        expect(item).to_have_attribute("aria-expanded", "false")
        expect(item).to_have_attribute("aria-controls", f"submenu-content-{menu_id}")

        # Icon is decorative
        icon = item.locator('svg[aria-hidden="true"]')
        expect(icon).to_be_visible()

        # Label text
        label = item.locator("p")
        expect(label).to_be_visible()
        expect(label).to_have_text(menu_id.capitalize())

        # Interactions
        item.click()
        submenu_container = nav_left.locator('div.submenu-container')
        expect(submenu_container).to_be_visible()
        expect(submenu_container).to_have_attribute("role", "region")
        expect(submenu_container).to_have_attribute("aria-live", "polite")

        # Submenu content
        submenu = nav_left.locator(".submenu")
        expect(submenu).to_be_visible()

        submenu_header = submenu.locator(".submenu-header")
        expect(submenu_header.locator("h1")).to_be_visible()
        expect(submenu_header.locator("ps-button")).to_be_visible()

        # Check submenu search input presence and placeholder
        search_input = submenu.locator("#submenu-search")
        expect(search_input).to_be_visible()
        placeholder = search_input.get_attribute("placeholder")
        assert "Search" in placeholder

        # Check submenu list role
        submenu_list = submenu.locator("#submenu-list")

        #Wait for submenu items to be rendered and check at least one exists
        submenu_items = submenu_list.locator("li.submenu-item")
        count = submenu_items.count()

        if count > 0:
            for i in range(count):
                data_item = submenu_items.nth(i)
                expect(data_item).to_be_visible()
                expect(data_item).to_have_class("submenu-item")
                
                # Icon is decorative
                icon = data_item.locator('svg[aria-hidden="true"]')
                expect(icon).to_be_visible()
                
                # Label text
                label = data_item.locator("h5")
                expect(label).to_be_visible()

                #interaction
                data_item.click()
                assert menu_id in p.url
                # Go back to home for next iteration
                p.go_back()   

        item.click()  # Close submenu   

def homepage_nav_shortcuts(p: Page) -> None:
    nav_left = p.get_by_role("navigation", name="Menu Navigation")
    expect(nav_left).to_be_visible()

def test_home():
    with sync_playwright() as playwright:

        # Launch the browser and open a new page
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://localhost:5001/")
        
        # Run the test function
        homepage_getting_started_heading(page)
        homepage_published_templates(page)
        homepage_nav_top(page)
        homepage_nav_left(page)
        homepage_nav_shortcuts(page)

        # Close the browser
        context.close()
        browser.close()
