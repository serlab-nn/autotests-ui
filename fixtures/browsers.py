import pytest
from playwright.sync_api import Playwright, Page, expect, sync_playwright


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
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
    context.storage_state(path="../browser-state.json")
    context.browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()

@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()