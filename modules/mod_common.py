import logging
from selenium.webdriver.common.by import By
from time import sleep
from data_storage import url_storage as url
from data_storage import xpath_storage as xpath




# 찾고자하는 element가 페이지에 존재하는지 확인. 있다면 True, 없다면 False 리턴
def is_element_exist(driver, xpath):
    if(driver.find_elements(By.XPATH, xpath).__len__() > 0):
        logging.info(xpath + "엘리먼트가 존재합니다.")
        return True
    else:
        logging.info(xpath + "엘리먼트가 존재하지 않습니다.")
        return False



# 현재 활성화된 페이지의 URL이 확인하고자하는 URL 값과 일치하는지 확인. 일치한다면 True, 다르다면 False 리턴
def compare_url(driver, url):
    current_url = driver.current_url

    logging.info("현재 URL : " + current_url)
    logging.info("비교 URL : " + url)
    if(current_url == url):
        logging.info("두 URL이 일치합니다.")
        return True
    else:
        logging.info("두 URL이 다릅니다.")
        return False


# 현재 페이지의 url에 string 문자열이 포함되어 있는지 확인. 포함된다면 True, 포함되지 않는다면 False 리턴
def contain_string_url(driver, string):
    current_url = driver.current_url
    
    if(current_url.__contains__(string) == True):
        logging.info(current_url + " 이 " + string + " 을 포함하고 있습니다.")
        return True
    else:
        logging.info(current_url + " 이 " + string + " 을 포함하고 있지않습니다.")
        return False


# 현재 페이지의 자동 더보기가 끝날 때까지(전체 리스트 노출까지) 스크롤 다운시켜 전체 리스트를 노출시킵니다.
# 스크롤 안정성을 위해 인위적으로 sleep(0.9)를 추가했습니다.
def scroll_down_until_end(driver):
    current_height = 0

    while(True):
        bottom = driver.execute_script("return document.body.scrollHeight")

        if (current_height < bottom):
            driver.execute_script("window.scrollTo(" + str(current_height) + ", " + str(bottom) + ")")
            current_height = bottom
            sleep(0.9)
        else:
            break


# 현재 페이지에서 xpath를 가진 element를 발견할 때까지 스크롤 다운을 진행합니다.
# 스크롤 안정성을 위해 인위적으로 sleep(0.9)를 추가했습니다.
def scroll_down_until_element_exist(driver, xpath):
    current_height = 0

    while(True):
        bottom = driver.execute_script("return document.body.scrollHeight")

        if (current_height < bottom and is_element_exist(driver, xpath) == False):
            driver.execute_script("window.scrollTo(" + str(current_height) + ", " + str(bottom) + ")")
            current_height = bottom
            sleep(0.9)
        else:
            break


# 현재 페이지에서 빠르게 5회의 스크롤 다운을 진행합니다.
def scroll_down_fast(driver):
    current_height = 0

    for i in range(0, 5):
        bottom = driver.execute_script("return document.body.scrollHeight")

        if(current_height < bottom):
            driver.execute_script("window.scrollTo(" + str(current_height) + ", " + str(bottom) + ")")
            current_height = bottom
            sleep(0.5)