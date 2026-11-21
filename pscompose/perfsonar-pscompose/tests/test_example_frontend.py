from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:5001/")
    elem = page.get_by_role("heading", name="Getting Started")
    assert elem.inner_html() == "Getting Started"

    # ---------------------
    context.close()
    browser.close()


# NB: pytest tests must start with 'test_'
def test_example_frontend():
    with sync_playwright() as playwright:
        run(playwright)
