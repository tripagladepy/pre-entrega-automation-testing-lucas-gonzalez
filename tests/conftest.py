import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Headless para GitHub Actions
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless=new")

    # Flags obligatorios para Linux CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Chrome del sistema (NO webdriver-manager en CI)
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    # Timeout global
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()


# Screenshot automático si falla un test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver", None)
    if not driver:
        return

    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{item.name}_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)

    extra = getattr(report, "extra", [])
    try:
        from pytest_html import extras
        extra.append(extras.image(file_path))
        report.extra = extra
    except ImportError:
        pass
