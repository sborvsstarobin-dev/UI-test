from playwright.sync_api import sync_playwright


def test_text_box(page):
    page.goto("https://demoqa.com/text-box")

    page.fill('#userName', 'Test')

    page.fill('input[placeholder="name@example.com"]', 'Test@mail.ru')

    page.fill('textarea#currentAddress', 'г. Москва ул. Шведский тупик 3')

    page.fill('textarea#permanentAddress', 'г. Москва ул. Шведский тупик 15')

    page.click("text=Submit")


