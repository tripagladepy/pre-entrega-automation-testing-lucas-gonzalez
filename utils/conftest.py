# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     yield driver
#     driver.quit()



# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import os

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()

#     # MODO NORMAL EN LOCAL
#     options.add_argument("--start-maximized")

#     # MODO HEADLESS EN GITHUB ACTIONS
#     if os.getenv("HEADLESS") == "true":
#         options.add_argument("--headless=new")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--window-size=1920,1080")

#     # Crear driver
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     yield driver
#     driver.quit()


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import os

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()

#     # MODO NORMAL EN TU PC
#     options.add_argument("--start-maximized")

#     # MODO HEADLESS EN GITHUB ACTIONS
#     if os.getenv("HEADLESS") == "true":
#         options.add_argument("--headless=new")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--window-size=1920,1080")

#     # Crear driver
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     yield driver
#     driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # En Github Actions → headless y binary_location obligatorio
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.binary_location = "/usr/bin/google-chrome-stable"

        # debug: print path del binario
        options.binary_location = "/usr/bin/google-chrome-stable"
        print("Using chrome binary:", options.binary_location)
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()
