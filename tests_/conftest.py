import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)


@pytest.fixture(scope='module')
def _drivers():
    driver = webdriver.Chrome(options=opts)
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(20)
    yield driver