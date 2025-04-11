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
    registration_page.fill_registration_form(email='user.name@gmail.com', password='password', username='username')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
