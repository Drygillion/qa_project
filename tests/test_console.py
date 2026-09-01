import pytest
import re
from playwright.sync_api import Page
from pages.console_page import ConsolePage


class TestConsole:
    """
    Тесты для проверки функциональности консоли Outerspace.
    """

    def test_page_loaded(self, page: Page):
        """
        Тест: проверка загрузки страницы.
        Проверяет заголовок и приветственное сообщение.
        """
        console = ConsolePage(page)
        console.navigate_to_console()

        # Проверяем заголовок через data-test-id
        title = console.get_title_text()
        assert "Outerspace" in title, f"Неверный заголовок: {title}"

        # Проверяем приветственное сообщение
        console.assert_output_contains("Welcome to the system console!")
        console.assert_output_contains("Type \"help\" to explore all available commands")

    def test_help_command(self, page: Page):
        """
        Тест: команда help должна показывать список команд.
        Проверяет наличие команд: help, clear, date.
        """
        console = ConsolePage(page)
        console.navigate_to_console()

        console.enter_command("help")
        console.assert_help_commands()

    def test_date_command(self, page: Page):
        """
        Тест: команда date должна показывать текущую дату и время.
        Проверяет формат: YYYY/MM/DD HH:MM:SS
        """
        console = ConsolePage(page)
        console.navigate_to_console()

        console.enter_command("date")
        output = console.get_full_output()

        # Ищем дату в формате: 2026/09/01 18:57:51
        date_pattern = r'\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}'
        has_date = bool(re.search(date_pattern, output))

        assert has_date, (
            f"Вывод команды date не содержит дату и время в формате YYYY/MM/DD HH:MM:SS. "
            f"Фактический вывод: {output}"
        )

    def test_clear_command(self, page: Page):
        """
        Тест: команда clear должна очищать консоль.
        Проверяет, что после clear вывод становится пустым или содержит только приветствие.
        """
        console = ConsolePage(page)
        console.navigate_to_console()

        # Сначала вводим help, чтобы появился вывод
        console.enter_command("help")
        console.assert_output_not_empty()

        # Очищаем консоль
        console.clear_console()

        # Проверяем, что вывод очистился
        console.assert_output_empty_or_welcome()

    def test_unknown_command(self, page: Page):
        """
        Тест: неизвестная команда должна выдавать сообщение об ошибке.
        Проверяет наличие ключевых слов ошибки в выводе.
        """
        console = ConsolePage(page)
        console.navigate_to_console()

        console.enter_command("unknown_command_123")
        output = console.get_full_output()

        # Ключевые слова, указывающие на ошибку
        error_keywords = ["unknown", "not found", "error", "incorrect", "неизвестн", "ошибк"]
        found_error = any(keyword in output.lower() for keyword in error_keywords)

        assert found_error, f"Не найдено сообщение об ошибке: {output}"