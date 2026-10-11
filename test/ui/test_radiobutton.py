from playwright.sync_api import sync_playwright, expect


def test_radiobutton(page):
    page.goto("https://demoqa.com/radio-button")

    yes_radio = page.get_by_role("radio", name="Yes")
    expect(yes_radio).to_be_visible()
    yes_radio.click()
    expect(yes_radio).to_be_checked()

    expect(page.locator(".text-success")).to_have_text("Yes")


