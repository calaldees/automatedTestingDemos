import pytest

from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_options(chrome_options):
    #CHROME_FLAGS = ("disable-gpu", "disable-infobars", "no-sandbox", "allow-insecure-localhost")
    CHROME_FLAGS = ('start-maximized', )
    for flag in CHROME_FLAGS:
        chrome_options.add_argument(f'--{flag}')
    return chrome_options


@pytest.fixture
def selenium(selenium):
    def wait_for_element(*args):
        return WebDriverWait(selenium, 10).until(EC.presence_of_element_located(args))
    selenium.wait_for_element = wait_for_element
    yield selenium
