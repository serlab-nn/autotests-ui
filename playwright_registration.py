from time import sleep
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')
    expect(email_input).to_have_value('user.name@gmail.com')

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')
    expect(username_input).to_have_value('username')

    # Заполняем поле password
    username_input = page.get_by_test_id('registration-form-password-input').locator('input')
    username_input.fill('password')
    expect(username_input).to_have_value('password')

    # Ожидание для визиуальной оценки заполнения полей
    sleep(3)

    # Нажимаем кнопку registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
    registration_button.click()

    # Проверяем заголовок dashboard
    expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()

    # Ожидание для визиуальной оценки отображения заголовка
    sleep(3)