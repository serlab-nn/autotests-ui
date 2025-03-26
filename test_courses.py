from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем форму
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')
        expect(email_input).to_have_value('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')
        expect(username_input).to_have_value('username')

        username_input = page.get_by_test_id('registration-form-password-input').locator('input')
        username_input.fill('password')
        expect(username_input).to_have_value('password')

        # Нажимаем на кнопку registration
        registration_button = page.get_by_test_id('registration-page-registration-button').click()

        # Сохраняем состояние браузера и убиваем текущую сессию браузера
        context.storage_state(path="browser-state.json")
        context.browser.close()

        # Переходим на Courses с сохраненным ранее контекстом
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверяем элементы на Courses
        expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        result_block = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_block).to_be_visible()
        expect(result_block).to_have_text('There is no results')
