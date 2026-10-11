from playwright.sync_api import sync_playwright


def test_select_date(page):
    page.goto("https://demoqa.com/date-picker")

    date_input = page.locator("#datePickerMonthYearInput")
    date_input.click()

    page.locator(".react-datepicker__month-select").select_option("7")
    page.locator(".react-datepicker__year-select").select_option("2025")
    page.locator(".react-datepicker__day--025").click()

    assert date_input.input_value() == "08/25/2025"


def test_date_and_time(page):
    page.goto("https://demoqa.com/date-picker")

    dat_input = page.locator("#dateAndTimePickerInput")
    dat_input.click()

    page.locator(".react-datepicker__month-read-view").click()
    page.locator(".react-datepicker__month-option>>text=August").click()

    page.locator(".react-datepicker__year-read-view").click()
    page.locator(".react-datepicker__year-option>>text = 2028").click()

    page.locator(".react-datepicker__day--021").click()

    page.locator(".react-datepicker__time-list-item >>text=03:00").click()

    value = dat_input.input_value()
    assert dat_input.input_value() == "August 21, 2028 3:00 AM"
