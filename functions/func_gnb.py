from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from data_storage import var_storage as var
from modules import mod_common
from modules import mod_enter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging



def gnb_enter_logo(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        driver.find_element(By.XPATH, xpath.gnb.logo).click()

        if(mod_common.compare_url(driver, url.page.service_home) == True):
            logging.info("Pass : GNB 요기요 로고를 통해 요기요 서비스 홈으로 이동했습니다.")
            return True
        else:
            raise Exception("GNB 요기요 로고 이동 실패")
    except:
        logging.error("Fail : GNB 요기요 로고를 통해 요기요 서비스 홈으로 이동하지 못했습니다.")
        return False



def gnb_enter_login(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        driver.find_element(By.XPATH, xpath.gnb.login_btn).click()

        if(mod_common.compare_url(driver, url.page.login) == True):
            logging.info("Pass : GNB 로그인 버튼을 통해 요기요 로그인 페이지로 이동했습니다.")
            return True
        else:
            raise Exception("GNB 로그인 이동 실패")
    except:
        logging.error("Fail : GNB 로그인 버튼을 통해 요기요 로그인 페이지로 이동하지 못했습니다.")
        return False



def gnb_exist_cart(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        if(mod_common.is_element_exist(driver, xpath.gnb.cart_btn) == True):
            logging.info("Pass : GNB 주문표 버튼이 노출됩니다.")
            return True
        else:
            raise Exception("GNB 주문표 버튼 미노출")
    except:
        logging.error("Fail : GNB 주문표 버튼이 미노출됩니다.")
        return False
