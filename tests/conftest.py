import pytest

@pytest.fixture
def chrome_options(chrome_options):
    #CHROME_FLAGS = ("disable-gpu", "disable-infobars", "no-sandbox", "allow-insecure-localhost")
    CHROME_FLAGS = ('start-maximized', )
    for flag in CHROME_FLAGS:
        chrome_options.add_argument(f'--{flag}')
    return chrome_options