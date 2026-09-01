import pytest
from playwright.sync_api import Browser, BrowserContext, Page
import os


@pytest.fixture(scope="function")
def browser_context(browser: Browser) -> BrowserContext:
    """Создание контекста браузера для каждого теста"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True,
        locale="ru-RU"
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(browser_context: BrowserContext) -> Page:
    """Создание страницы для каждого теста"""
    page = browser_context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)


def pytest_configure(config):
    """Настройка перед запуском тестов"""
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)