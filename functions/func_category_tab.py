from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from data_storage import var_storage as var
from modules import mod_common
from modules import mod_enter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging



def category_enter_all(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_all = categories[0]

        tab_all.click()
        if(mod_common.compare_url(driver, url.category.all) == True):
            logging.info("Pass : 카테고리 탭을 통해 전체보기 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 전체보기 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 전체보기 탭으로 이동하지 못했습니다.")
        return False



def category_enter_one(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_one = categories[1]

        tab_one.click()
        if(mod_common.compare_url(driver, url.category.one) == True):
            logging.info("Pass : 카테고리 탭을 통해 1인분 주문 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 1인분 주문 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 1인분 주문 탭으로 이동하지 못했습니다.")
        return False



def category_enter_franchise(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_franchise = categories[2]

        tab_franchise.click()
        if(mod_common.compare_url(driver, url.category.franchise) == True):
            logging.info("Pass : 카테고리 탭을 통해 프랜차이즈 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 프랜차이즈 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 프랜차이즈 탭으로 이동하지 못했습니다.")
        return False



def category_enter_chicken(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_chicken = categories[3]

        tab_chicken.click()
        if(mod_common.compare_url(driver, url.category.chicken) == True):
            logging.info("Pass : 카테고리 탭을 통해 치킨 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 치킨 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 치킨 탭으로 이동하지 못했습니다.")
        return False



def category_enter_western(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_western = categories[4]

        tab_western.click()
        if(mod_common.compare_url(driver, url.category.western) == True):
            logging.info("Pass : 카테고리 탭을 통해 피자/양식 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 피자/양식 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 피자/양식 탭으로 이동하지 못했습니다.")
        return False



def category_enter_chinese(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_chinese = categories[5]

        tab_chinese.click()
        if(mod_common.compare_url(driver, url.category.chinese) == True):
            logging.info("Pass : 카테고리 탭을 통해 중국집 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 중국집 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 중국집 탭으로 이동하지 못했습니다.")
        return False



def category_enter_korean(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_korean = categories[6]

        tab_korean.click()
        if(mod_common.compare_url(driver, url.category.korean) == True):
            logging.info("Pass : 카테고리 탭을 통해 한식 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 한식 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 한식 탭으로 이동하지 못했습니다.")
        return False




def category_enter_japanese(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_japanese = categories[7]

        tab_japanese.click()
        if(mod_common.compare_url(driver, url.category.japanese) == True):
            logging.info("Pass : 카테고리 탭을 통해 일식/돈까스 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 일식/돈까스 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 일식/돈까스 탭으로 이동하지 못했습니다.")
        return False




def category_enter_pork(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_pork = categories[8]

        tab_pork.click()
        if(mod_common.compare_url(driver, url.category.pork) == True):
            logging.info("Pass : 카테고리 탭을 통해 족발/보쌈 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 족발/보쌈 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 족발/보쌈 탭으로 이동하지 못했습니다.")
        return False




def category_enter_night(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_night = categories[9]

        tab_night.click()
        if(mod_common.compare_url(driver, url.category.night) == True):
            logging.info("Pass : 카테고리 탭을 통해 야식 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 야식 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 야식 탭으로 이동하지 못했습니다.")
        return False




def category_enter_snack(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_snack = categories[10]

        tab_snack.click()
        if(mod_common.compare_url(driver, url.category.snack) == True):
            logging.info("Pass : 카테고리 탭을 통해 분식 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 분식 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 분식 탭으로 이동하지 못했습니다.")
        return False




def category_enter_cafe(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_cafe = categories[11]

        tab_cafe.click()
        if(mod_common.compare_url(driver, url.category.cafe) == True):
            logging.info("Pass : 카테고리 탭을 통해 카페/디저트 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 카페/디저트 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 카페/디저트 탭으로 이동하지 못했습니다.")
        return False




def category_enter_mart(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        categories = driver.find_elements(By.XPATH, xpath.category.tabs)
        tab_mart = categories[12]

        tab_mart.click()
        if(mod_common.compare_url(driver, url.category.mart) == True):
            logging.info("Pass : 카테고리 탭을 통해 편의점/마트 탭으로 이동했습니다.")
            return True
        else:
            raise Exception("카테고리 편의점/마트 탭 이동 실패")
    except:
        logging.error("Fail : 카테고리 탭을 통해 편의점/마트 탭으로 이동하지 못했습니다.")
        return False