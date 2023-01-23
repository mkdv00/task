import pytest

from selene.support.shared import browser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.driver.maximize_window()
    yield
    browser.quit()
