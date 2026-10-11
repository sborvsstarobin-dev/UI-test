from playwright.sync_api import sync_playwright, expect


def test_practice_form(page, tmp_path):
    page.goto("https://demoqa.com/automation-practice-form")

    page.fill("#firstName", "Alex")
    page.fill("#lastName", "Kotl")
    page.fill("#userEmail", "bystree@mail.ru")

    page.locator('label[for="gender-radio-1"]').click()

    page.fill("#userNumber", "9992345678")

    date_input = page.locator("#dateOfBirthInput")
    date_input.click()
    page.locator(".react-datepicker__month-select").select_option("4")
    page.locator(".react-datepicker__year-select").select_option("2020")
    page.locator(".react-datepicker__day--017").click()

    subjects_input = page.locator("#subjectsInput")
    subjects_input.fill("History")

    page.get_by_role("checkbox", name="Sports").click(force=True)

    file_path = tmp_path / "demoqa_test_file.txt"
    file_path.write_text("Hello, this is a test file for DemoQA upload!")
    page.set_input_files("#uploadPicture", str(file_path))

    page.fill("#currentAddress", "Moscow")

    page.locator("#state").click()
    page.locator("div[id^='react-select-3-option']:has-text('NCR')").click()

    page.locator("#city").click()
    page.locator("div[id^='react-select-4-option']:has-text('Delhi')").click()

    page.locator("#submit").click()


