from playwright.sync_api import sync_playwright


def test_checkbox(page):
    page.goto("https://demoqa.com/checkbox")

    page.locator(".rc-tree-switcher.rc-tree-switcher_close").click()

    page.locator("span[aria-label='Select Desktop']").check()
    page.locator("span[aria-label='Select Documents']").check()
    page.locator("span[aria-label='Select Downloads']").check()

    result = page.locator("#result").inner_text()
    assert "home" in result

