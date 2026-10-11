from playwright.sync_api import sync_playwright, expect


def test_alert_button(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "You clicked a button"
        dialog.accept()

    page.once("dialog", handle_alert)

    page.locator("#alertButton").click()


def test_timer_alert_button(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "This alert appeared after 5 seconds"
        dialog.accept()

    page.locator("#timerAlertButton").click()

    page.wait_for_event("dialog", timeout=6000)



def test_confirm_button_yes(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "Do you confirm action?"
        dialog.accept()

    page.once("dialog", handle_alert)

    page.locator("#confirmButton").click()

    expect(page.locator("#confirmResult")).to_have_text("You selected Ok")


def test_confirm_button_no(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "Do you confirm action?"
        dialog.dismiss()

    page.once("dialog", handle_alert)

    page.locator("#confirmButton").click()

    expect(page.locator("#confirmResult")).to_have_text("You selected Cancel")


def test_promt_button(page):
    page.goto("https://demoqa.com/alerts")

    def handle_alert(dialog):
        assert dialog.message == "Please enter your name"
        dialog.accept("hello")

    page.once("dialog", handle_alert)

    page.locator("#promtButton").click()

    expect(page.locator("#promptResult")).to_have_text("You entered hello")
