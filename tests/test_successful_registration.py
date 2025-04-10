import time

import pytest
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, password, username",
    [
        ("user.name@gmail.com", "password", "username")
    ]
)
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str,
        password: str,
        username: str
):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, password=password, username=username)
    registration_page.click_registration_button()
    """Я заметил, что при переходе в часть Dashboard, последующий код не отрабатывает, т.к. тест всегда 
    PASSED, даже если указать явно провальные проверки, например expect(self.dashboard_title).not_to_be_visible().
    Понимаю, что использовать подобное ожидание неверно, но я не понимаю, почему без него тест работает некорректно,
    будто все что после registration_page игнорируется"""
    time.sleep(3)
    dashboard_page.check_visible_dashboard_title()
