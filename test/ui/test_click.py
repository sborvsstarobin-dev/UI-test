from playwright.sync_api import sync_playwright, expect


def test_click(page):
    page.goto("https://demoqa.com/buttons")

    db_click = page.get_by_role("button", name="Double Click Me", exact=True)
    expect(db_click).to_be_visible()
    db_click.dblclick()
    expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")

    right_click = page.get_by_role("button", name="Right Click Me", exact=True)
    expect(right_click).to_be_visible()
    right_click.click(button="right")
    expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")

    one_click = page.get_by_role("button", name="Click Me", exact=True)
    expect(one_click).to_be_visible()
    one_click.click()
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")


