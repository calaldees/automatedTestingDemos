import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def selenium_bbc(selenium):
    selenium.get('http://www.bbc.co.uk')
    assert 'Home' in selenium.title
    return selenium


def test_bbc_top_story(selenium_bbc):
    selenium = selenium_bbc
    selenium.wait_for_element(By.CSS_SELECTOR, '.top-story').click()
    assert selenium.wait_for_element(By.CSS_SELECTOR, '.story-body__h1').text, 'Article should have a title'
    assert selenium.wait_for_element(By.CSS_SELECTOR, '.media-with-caption'), 'Article should have an image/video'


def test_bbc_terms(selenium_bbc):
    selenium = selenium_bbc
    selenium.wait_for_element(By.PARTIAL_LINK_TEXT, 'Terms of Use').click()
    assert 'When do I need a TV Licence' in selenium.page_source
    assert 'When do I need a TV Licence' in selenium.wait_for_element(By.CSS_SELECTOR, '.gel-layout.gel-topic-opts').text
