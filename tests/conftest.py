import os
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):   #Guarda screenshot si un test falla y lo adjunta al reporte HTML.
   
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver", None)
    if not driver:
        return

    screenshots_dir = "reports/screenshots"   # carpeta donde guardar imágenes
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")   
    file_name = f"{item.name}_{timestamp}.png"   # nombre del archivo
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)   # guarda screenshot

    extra = getattr(report, "extra", [])   # adjuntar al HTML (si pytest-html está presente)
    try:
        from pytest_html import extras
        extra.append(extras.image(file_path))
        report.extra = extra
    except ImportError:
        pass
