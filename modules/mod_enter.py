import logging
from selenium.webdriver.common.by import By
from time import sleep
from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from modules import mod_common


# 레스토랑 리스트 페이지를 진입하는 함수입니다.
# 요기요 서비스 홈으로 진입하여 위치 입력창에 설정한 주소값을 넣고 검색하여 레스토랑 리스트 페이지로 진입합니다.
def enter_restaurant_list(driver, address):
    try:
        driver.get(url.page.service_home)
        sleep(0.5)

        driver.find_element(By.XPATH, xpath.search.input).clear()
        driver.find_element(By.XPATH, xpath.search.input).send_keys(address)
        driver.find_element(By.XPATH, xpath.search.searching_button).click()
        sleep(1.5)
        if(mod_common.compare_url(driver, url.page.restaurant_home) == True):
            logging.info("Success : 레스토랑 리스트 페이지 진입에 성공했습니다.")
        else:
            logging.error("Error! 레스토랑 리스트 페이지가 아닌 다른 리스트 페이지에 진입했습니다.")
    except:
        logging.error("Error! 레스토랑 리스트 페이지 진입에 실패했습니다.")