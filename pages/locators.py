
class ConsoleLocators:
    """Селекторы для страницы консоли"""

    # data-test-id селекторы
    TITLE = '[data-test-id="console-title"]'
    OUTPUT_AREA = '[data-test-id="console-output"]'
    INPUT_LINE = '[data-test-id="console-input"] input'

    # Тексты для проверок
    WELCOME_TEXT = "Welcome to the system console!"
    HELP_HINT_TEXT = 'Type "help" to explore all available commands'
    HELP_OUTPUT_MARKER = "BEHOLD!"
    DATE_OUTPUT_MARKER = "Oracle of Time"

    # Команды
    HELP_COMMAND = "help"
    CLEAR_COMMAND = "clear"
    DATE_COMMAND = "date"

    # Формат даты
    DATE_PATTERN = r'\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}'

    # Ключевые слова ошибок
    ERROR_KEYWORDS = ["unknown", "not found", "error", "incorrect", "неизвестн", "ошибк"]