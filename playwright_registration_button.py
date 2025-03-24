from time import sleep
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Проверяем состояние кнопки registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

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

    # Проверяем состояние кнопки registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_disabled()
