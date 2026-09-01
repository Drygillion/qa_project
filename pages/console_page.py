from pages.base_page import BasePage
from pages.locators import ConsoleLocators
from playwright.sync_api import Page
import re


class ConsolePage(BasePage):
    """
    Page Object для страницы консоли.
    """

    URL = "https://exam.space-qa.site/"


    def navigate_to_console(self):
        self.navigate(self.URL)
        self.wait_for_element(ConsoleLocators.INPUT_LINE)
        return self

    def enter_command(self, command: str):
        self.fill(ConsoleLocators.INPUT_LINE, command)
        self.press_enter(ConsoleLocators.INPUT_LINE)
        self.page.wait_for_timeout(500)
        return self

    def get_full_output(self) -> str:
        return self.get_text(ConsoleLocators.OUTPUT_AREA)

    def get_title_text(self) -> str:
        return self.get_text(ConsoleLocators.TITLE)

    def clear_console(self):
        self.enter_command(ConsoleLocators.CLEAR_COMMAND)
        return self

    def assert_output_contains(self, expected_text: str):
        output = self.get_full_output()
        assert expected_text in output, f"Вывод не содержит '{expected_text}'. Вывод: {output}"
        return self

    def assert_output_not_empty(self):
        output = self.get_full_output()
        assert len(output.strip()) > 0, "Вывод пустой"
        return self

    def assert_output_empty_or_welcome(self):
        output_lines = [line.strip() for line in self.get_full_output().split('\n') if line.strip()]
        assert len(output_lines) <= 3, f"Вывод содержит больше 3 строк: {len(output_lines)}"
        return self

    def assert_help_commands(self):
        output = self.get_full_output()
        expected_commands = [
            ConsoleLocators.HELP_COMMAND,
            ConsoleLocators.CLEAR_COMMAND,
            ConsoleLocators.DATE_COMMAND
        ]
        for cmd in expected_commands:
            assert cmd in output, f"Команда '{cmd}' не найдена"

        assert ConsoleLocators.HELP_OUTPUT_MARKER in output, "Нет маркера BEHOLD!"
        assert ConsoleLocators.DATE_OUTPUT_MARKER in output, "Нет маркера Oracle of Time"
        return self

    def assert_date_format(self):
        output = self.get_full_output()
        has_date = bool(re.search(ConsoleLocators.DATE_PATTERN, output))
        assert has_date, f"Дата не найдена. Вывод: {output}"
        return self

    def assert_error_message(self):
        output = self.get_full_output()
        found = any(kw in output.lower() for kw in ConsoleLocators.ERROR_KEYWORDS)
        assert found, f"Ошибка не найдена. Вывод: {output}"
        return self