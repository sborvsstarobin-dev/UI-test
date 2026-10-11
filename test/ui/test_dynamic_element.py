from playwright.sync_api import sync_playwright, expect


def test_dynamic_element(page):
    page.goto("https://demoqa.com/dynamic-properties")

    dynamic_button = page.locator("#visibleAfter")
    expect(dynamic_button).to_be_visible(timeout=6000)
    dynamic_button.click()

    enable_button = page.locator("#enableAfter")
    expect(enable_button).to_be_visible(timeout=6000)
    enable_button.click()


