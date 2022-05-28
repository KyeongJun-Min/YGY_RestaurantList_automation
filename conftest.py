from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


# 초기화 영역입니다.
# 매 test case를 실행할 때마다 동일한 환경에서 test를 진행하기 위해 설정합니다.
@pytest.fixture(autouse=True, scope="function")
def driver():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver

    chrome_driver.quit()