from playwright.sync_api import Page
from typing import Optional


class BasePage:
    """
    Базовый класс для всех страниц.

    """

    def __init__(self, page: Page):
        self.page = page
        self._timeout = 10000

    def navigate(self, url: str):
        """Перейти по URL"""
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def locator(self, selector: str):
        """Универсальный метод для любого селектора"""
        return self.page.locator(selector)

    def wait_for_element(self, selector: str, timeout: Optional[int] = None):
        """Ожидать появления элемента"""
        timeout = timeout or self._timeout
        self.locator(selector).wait_for(state="visible", timeout=timeout)
        return self

    def fill(self, selector: str, text: str):
        """Заполнить поле ввода"""
        self.locator(selector).fill(text)
        return self

    def click(self, selector: str):
        """Кликнуть на элемент"""
        self.locator(selector).click()
        return self

    def get_text(self, selector: str) -> str:
        """Получить текст элемента"""
        return self.locator(selector).inner_text()

    def press_enter(self, selector: str):
        """Нажать Enter в поле ввода"""
        self.locator(selector).press("Enter")
        return self

    def is_visible(self, selector: str) -> bool:
        """Проверить, видим ли элемент"""
        try:
            return self.locator(selector).is_visible()
        except Exception:
            return False