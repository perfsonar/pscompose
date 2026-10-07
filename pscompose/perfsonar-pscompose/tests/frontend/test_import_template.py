import requests
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5001"
API_BASE = "http://localhost:8000/api"


# ── Structure tests ────────────────────────────────────────────────────────────


def import_page_heading(page: Page) -> None:
    """Import page renders the heading and description."""
    page.goto(f"{BASE_URL}/import/")
    page.wait_for_load_state("networkidle")

    import_page = page.locator(".import-page")
    expect(import_page).to_be_visible(timeout=10_000)

    heading = import_page.locator("h3")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Import Template")

    desc = import_page.locator("p")
    expect(desc).to_be_visible()
    expect(desc).to_contain_text("import via URL link or file upload")


def import_page_form_structure(page: Page) -> None:
    """Import page renders the JSON form and action buttons."""
    page.goto(f"{BASE_URL}/import/")

    import_page = page.locator(".import-page")
    expect(import_page).to_be_visible(timeout=10_000)

    form = import_page.locator("#template-import-form")
    expect(form).to_be_visible()

    # JSON Forms element
    json_form = form.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)

    # Save button
    save_btn = form.locator("#save-btn")
    expect(save_btn).to_be_visible()
    expect(save_btn).to_have_attribute("label", "Save")
    expect(save_btn).to_have_attribute("theme", "Secondary")
    expect(save_btn).to_have_attribute("confirm-modal", "save-modal")

    # Cancel button
    cancel_btn = form.locator("ps-button[label='Cancel']")
    expect(cancel_btn).to_be_visible()
    expect(cancel_btn).to_have_attribute("theme", "Primary")


def import_page_save_modal_present(page: Page) -> None:
    """Save and delete modals are injected on the import page."""
    page.goto(f"{BASE_URL}/import/")

    save_modal = page.locator("#save-modal")
    expect(save_modal).to_be_attached()

    delete_modal = page.locator("#delete-modal")
    expect(delete_modal).to_be_attached()


def import_page_empty_submit_stays_on_page(page: Page) -> None:
    """Submitting an empty import form stays on the import page."""
    page.goto(f"{BASE_URL}/import/")

    json_form = page.locator("json-form")
    expect(json_form).to_be_visible(timeout=10_000)

    save_btn = page.locator("#save-btn")
    expect(save_btn).to_be_visible()
    save_btn.click()
    page.wait_for_timeout(500)

    # Still on import page
    assert "/import/" in page.url

    # Save modal should NOT open (form failed validation)
    save_modal = page.locator("#save-modal")
    expect(save_modal).not_to_have_attribute("open", "")


def import_page_cancel_navigates_back(page: Page) -> None:
    """Clicking Cancel on the import page navigates back."""
    # Navigate from home first so there is a history entry to go back to
    page.goto(f"{BASE_URL}/")
    page.wait_for_load_state("networkidle")

    page.goto(f"{BASE_URL}/import/")

    import_page = page.locator(".import-page")
    expect(import_page).to_be_visible(timeout=10_000)

    cancel_btn = page.locator("ps-button[label='Cancel']")
    expect(cancel_btn).to_be_visible(timeout=5_000)
    cancel_btn.click()
    page.wait_for_timeout(500)

    # Should have navigated away from /import/
    assert "/import/" not in page.url or page.url == f"{BASE_URL}/"


# ── Navigation bar on import page ─────────────────────────────────────────────


def import_page_nav_top_visible(page: Page) -> None:
    """Top navigation is visible on the import page."""
    page.goto(f"{BASE_URL}/import/")

    nav_top = page.get_by_role("navigation", name="Top Navigation")
    expect(nav_top).to_be_visible()

    logo = nav_top.get_by_role("link", name="Go to homepage")
    expect(logo).to_be_visible()

    readme_link = nav_top.get_by_role("link", name="README")
    expect(readme_link).to_be_visible()


def import_page_no_subnav(page: Page) -> None:
    """Subnav panel is closed on the import page."""
    page.goto(f"{BASE_URL}/import/")
    page.wait_for_load_state("networkidle")

    subnav_container = page.locator(".subnav-container")
    expect(subnav_container).not_to_have_class("open")


# ── Post-import success view ───────────────────────────────────────────────────


def import_page_success_view(page: Page) -> None:
    """After a successful import, the page shows a success heading and read form."""
    # Create a template via API to simulate an already-imported template
    r = requests.post(
        f"{API_BASE}/template/",
        json={
            "ref_set": [],
            "type": "psconfig",
            "json": {
                "addresses": {
                    "atla-ps-lat.lsst.es.net": {
                        "address": "atla-ps-lat.lsst.es.net",
                        "host": "atla-ps.es.net",
                        "_meta": {
                            "display-name": "atla-ps-lat.lsst.es.net",
                            "display-set": "atla-ps.lsst.es.net",
                        },
                    },
                    "chat-ps-lat.lsst.es.net": {
                        "address": "chat-ps-lat.lsst.es.net",
                        "host": "chat-ps.es.net",
                        "_meta": {
                            "display-name": "chat-ps-lat.lsst.es.net",
                            "display-set": "chat-ps.es.lsst.net",
                        },
                    },
                    "slac50n-ps-lat.lsst.es.net": {
                        "address": "slac50n-ps-lat.lsst.es.net",
                        "host": "slac50n-ps.es.net",
                        "_meta": {
                            "display-name": "slac50n-ps-lat.lsst.es.net",
                            "display-set": "slac50n-ps.lsst.es.net",
                        },
                    },
                    "slac50s-ps-lat.lsst.es.net": {
                        "address": "slac50s-ps-lat.lsst.es.net",
                        "host": "slac50s-ps.es.net",
                        "disabled": False,
                        "no-agent": False,
                        "_meta": {
                            "display-name": "slac50s-ps-lat.lsst.es.net",
                            "display-set": "slac50s-ps.lsst.es.net",
                        },
                    },
                    "perfsonar1-360.ls.lsst.org": {
                        "address": "perfsonar1-360.ls.lsst.org",
                        "host": "perfsonar1-360.ls.lsst.org",
                        "_meta": {
                            "display-name": "perfsonar1-360.ls.lsst.org",
                            "display-set": "perfsonar1-360.ls.lsst.org",
                        },
                    },
                    "ps-mia-lsr-lt.srv.ampath.net": {
                        "address": "ps-mia-lsr-lt.srv.ampath.net",
                        "host": "ps-mia-lsr-lt.srv.ampath.net",
                        "_meta": {
                            "display-name": "ps-mia-lsr-lt.srv.ampath.net-DNS",
                            "display-set": "ps-mia-lsr-lt.srv.ampath.net-DNS",
                        },
                    },
                    "ps-mia-lsr-lt.srv.ampath.net-IP": {
                        "address": "198.32.252.195",
                        "host": "ps-mia-lsr-lt.srv.ampath.net-IP",
                        "_meta": {
                            "display-name": "ps-mia-lsr-lt.srv.ampath.net-IP",
                            "display-set": "ps-mia-lsr-lt.srv.ampath.net-IP",
                        },
                    },
                    "psnr-oct-v40.slac.stanford.edu": {
                        "address": "psnr-oct-v40.slac.stanford.edu",
                        "host": "psnr-oct-v40.slac.stanford.edu",
                        "disabled": False,
                        "no-agent": False,
                        "_meta": {
                            "display-name": "psnr-oct-v40.slac.stanford.edu",
                            "display-set": "psnr-oct-v40.slac.stanford.eduu",
                        },
                    },
                },
                "groups": {
                    "group_lsst_latency": {
                        "type": "disjoint",
                        "a-addresses": [
                            {"name": "atla-ps-lat.lsst.es.net"},
                            {"name": "chat-ps-lat.lsst.es.net"},
                            {"name": "slac50n-ps-lat.lsst.es.net"},
                            {"name": "slac50s-ps-lat.lsst.es.net"},
                            {"name": "perfsonar1-360.ls.lsst.org"},
                            {"name": "ps-mia-lsr-lt.srv.ampath.net"},
                            {"name": "ps-mia-lsr-lt.srv.ampath.net-IP"},
                            {"name": "atla-ps-lat.lsst.es.net"},
                            {"name": "psnr-oct-v40.slac.stanford.edu"},
                        ],
                        "b-addresses": [
                            {"name": "atla-ps-lat.lsst.es.net"},
                            {"name": "chat-ps-lat.lsst.es.net"},
                            {"name": "slac50n-ps-lat.lsst.es.net"},
                            {"name": "slac50s-ps-lat.lsst.es.net"},
                            {"name": "perfsonar1-360.ls.lsst.org"},
                        ],
                    }
                },
                "tests": {
                    "ESnet6_LAT_1_v4": {
                        "type": "latencybg",
                        "spec": {
                            "spec": {
                                "dest": "{% address[1] %}",
                                "dest-node": "{% pscheduler_address[1] %}",
                                "flip": "{% flip %}",
                                "packet-count": 600,
                                "packet-interval": 0.1,
                                "packet-padding": 0,
                                "source": "{% address[0] %}",
                                "source-node": "{% pscheduler_address[0] %}",
                                "ip-version": 4,
                            }
                        },
                    }
                },
                "tasks": {
                    "LSST_IPv4_Loss_Testing": {
                        "reference": {
                            "display-set-source": '{% jq .addresses[0]._meta."display-set" %}',
                            "display-set-dest": '{% jq .addresses[1]._meta."display-set" %}',
                            "display-task-name": '{% jq .task._meta."display-name" %}',
                            "display-task-group": ["75: ESnet to LSST"],
                        },
                        "_meta": {
                            "display-name": "ESnet to LSST Networking IPv4 Packet Loss Testing"
                        },
                        "test": "ESnet6_LAT_1_v4",
                        "group": "group_lsst_latency",
                    }
                },
            },
            "name": "pw-import-test",
            "created_by": "playwright",
            "last_edited_by": "playwright",
        },
    )
    r.raise_for_status()
    item_id = r.json()["id"]

    try:
        # The success view is reached when ?id= is present on the import URL
        page.goto(f"{BASE_URL}/import/?id={item_id}")
        page.wait_for_load_state("networkidle")

        import_page = page.locator(".import-page")
        expect(import_page).to_be_visible(timeout=10_000)

        heading = import_page.locator("h3")
        expect(heading).to_be_visible()
        expect(heading).to_have_text("Success! Your template has been saved.")

        # Read form is shown
        read_form = page.locator(".datatype")
        expect(read_form).to_be_visible(timeout=10_000)
    finally:
        requests.delete(f"{API_BASE}/template/{item_id}/")


# ── Entry point ────────────────────────────────────────────────────────────────


def test_import_template(page: Page) -> None:
    import_page_heading(page)
    import_page_form_structure(page)
    import_page_save_modal_present(page)
    import_page_empty_submit_stays_on_page(page)
    import_page_cancel_navigates_back(page)
    import_page_nav_top_visible(page)
    import_page_no_subnav(page)
    import_page_success_view(page)
