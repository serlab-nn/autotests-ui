import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        # Переходим на Courses с сохраненным ранее контекстом
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверяем элементы на Courses
        expect(chromium_page_with_state).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        result_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_block).to_be_visible()
        expect(result_block).to_have_text('There is no results')
