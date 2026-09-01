# QA Project

Автотесты для сайта [https://exam.space-qa.site/](https://exam.space-qa.site/).  
Реализовано с использованием **Page Object Model** на связке **Python + Pytest + Playwright**.

---

## Что проверяют тесты

- Загрузка страницы и отображение приветствия
- Команды: `help`, `date`, `clear`
- Реакция на неизвестную команду
- Автоматический скриншот при падении теста

---

## Быстрый старт

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Установить браузер
playwright install chromium

# 3. Запустить все тесты
pytest -v

# 4. Запустить с HTML-отчётом
pytest --html=reports/report.html --self-contained-html
```

### Запуск с видимым браузером (для отладки)

```bash
pytest --headed --slowmo 500 -v
```

- `--headed` — показать браузер  
- `--slowmo 500` — замедлить выполнение (в мс)

---

## Отчёты

После запуска тестов в папке `reports/` появляются:

- `report.html` — HTML-отчёт с результатами тестов
- `screenshots/` — скриншоты упавших тестов

### Как открыть HTML-отчёт

1. В панели проекта найдите файл `reports/report.html`
2. Нажмите на него **правой кнопкой мыши**
3. Выберите **Open in Browser** → **Chrome** (или другой браузер)

Или просто дважды кликните по файлу — он откроется в браузере по умолчанию.

---

## Структура проекта

```text
qa_project/
├── pages/
│   ├── base_page.py       # общие методы для страниц
│   ├── console_page.py    # логика консоли
│   └── locators.py        # все селекторы в одном месте
├── tests/
│   ├── conftest.py        # фикстуры и хуки pytest
│   └── test_console.py    # тесты
├── reports/               # отчёты и скриншоты (создаётся автоматически)
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Технологии

- Python 3.11+
- Pytest
- Playwright
- Allure 

---