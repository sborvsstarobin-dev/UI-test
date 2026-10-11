def test_automation_practice_form_stable_complete(page):
    page.goto("https://demoqa.com/automation-practice-form")

    # Заполняем имя и фамилию
    page.get_by_placeholder("First Name").fill("Andrew")
    page.get_by_placeholder("Last Name").fill("U")

    # Заполняем почту
    page.get_by_placeholder("name@example.com").fill("theBest@example.com")

    # Выставляем гендер
    page.locator("label[for='gender-radio-2']").click()

    # Заполняем номер телефона
    page.get_by_placeholder("Mobile Number").fill("8888888889")

    # Проставляем дату
    date_input = page.locator("#dateOfBirthInput")
    date_input.click()
    page.locator(".react-datepicker__month-select").select_option("7")
    page.locator(".react-datepicker__year-select").select_option("2025")
    page.locator(".react-datepicker__day--008:not(.react-datepicker__day--outside-month)").click()

    assert "08 Aug 2025" in date_input.input_value()

    # Заполняем предмет
    subjects_input = page.locator("#subjectsInput")
    subjects_input.fill("Maths")

    # Выбираем хобби
    page.get_by_role("checkbox", name="Music").click(force=True)

    # Пишем адрес
    page.get_by_placeholder("Current Address").fill("123 Test Street")

    # Выбираем штат
    page.locator("#state").click()
    page.locator("div[id^='react-select-3-option']:has-text('NCR')").click()

    # Выбираем город
    page.locator("#city").click()
    page.locator("div[id^='react-select-4-option']:has-text('Delhi')").click()

    # Жмем на "Submit"
    page.locator("#submit").click()
    page.pause()