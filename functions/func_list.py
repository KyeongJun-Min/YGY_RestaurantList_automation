from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from data_storage import var_storage as var
from modules import mod_common
from modules import mod_enter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


# 레스토랑 리스트 최초 진입 시, 60개의 항목이 노출되는 것을 이용해 레스토랑 항목들이 노출되는지 확인합니다.
def list_count_first(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        counts = driver.find_elements(By.XPATH, xpath.list.items).__len__()

        logging.info("Pass : 레스토랑 리스트 최초 진입 시, " + str(counts) + "개의 가게 리스트가 정상적으로 노출됐습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트 최초 진입 시, 가게 리스트가 정상적으로 노출되지 않았습니다.")
        return False


# 레스토랑 리스트에 진입 후 끝까지 스크롤하여 자동 더보기를 진행합니다.
def list_count_scroll(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        mod_common.scroll_down_until_end(driver)

        counts = driver.find_elements(By.XPATH, xpath.list.items).__len__()

        logging.info("Pass : 레스토랑 리스트 진입 > 자동 스크롤 후, " + str(counts) + "개의 가게 리스트가 정상적으로 노출됐습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트 진입 > 자동 스크롤 후, 가게 리스트가 정상적으로 노출되지 않았습니다.")
        return False



def area_exist_advertisement(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        if(mod_common.is_element_exist(driver, xpath.list.advertisement_area) == True):
            logging.info("Pass : 레스토랑 리스트에 우리동네 플러스 영역이 정상적으로 노출됐습니다.")
            return True
        else:
            raise Exception("우리동네 플러스 영역 미노출")
    except:
        logging.error("Fail : 레스토랑 리스트에 우리동네 플러스 영역이 노출되지 않았습니다.")
        return False



def area_click_advertisement_tooltip(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        if(mod_common.is_element_exist(driver, xpath.list.advertisement_btn) == True):
            driver.find_element(By.XPATH, xpath.list.advertisement_btn).click()

            logging.info("Pass : 레스토랑 리스트의 우리동네 플러스 툴팁을 정상 클릭했습니다.")
            return True
        else:
            raise Exception("우리동네 플러스 툴팁 미노출")

    except:
        logging.error("Fail : 레스토랑 리스트의 우리동네 플러스 툴팁을 클릭하지 못했습니다.")
        return False



def area_exist_redweek(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        mod_common.scroll_down_until_element_exist(driver, xpath.list.redweek_area)

        if(mod_common.is_element_exist(driver, xpath.list.redweek_area) == True):
            logging.info("Pass : 레스토랑 리스트에 슈퍼레드위크 추천 영역이 정상적으로 노출됐습니다.")
            return True
        else:
            raise Exception("슈퍼레드위크 추천 영역 미노출")
    except:
        logging.error("Fail : 레스토랑 리스트에 슈퍼레드위크 추천 영역이 노출되지 않았습니다.")
        return False



def area_exist_registered(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        mod_common.scroll_down_until_element_exist(driver, xpath.list.registered_area)

        if(mod_common.is_element_exist(driver, xpath.list.registered_area) == True):
            logging.info("Pass : 레스토랑 리스트에 요기요 등록 음식점 영역이 정상적으로 노출됐습니다.")
            return True
        else:
            raise Exception("요기요 등록 음식점 영역 미노출")
    except:
        logging.error("Fail : 레스토랑 리스트에 요기요 등록 음식점 영역이 노출되지 않았습니다.")
        return False



def area_click_registered_tooltip(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        mod_common.scroll_down_until_element_exist(driver, xpath.list.registered_btn)

        if(mod_common.is_element_exist(driver, xpath.list.registered_btn) == True):
            driver.find_element(By.XPATH, xpath.list.registered_btn).click()

            logging.info("Pass : 레스토랑 리스트의 요기요 등록 음식점 툴팁을 정상 클릭했습니다.")
            return True
        else:
            raise Exception("요기요 등록 음식점 툴팁 미노출")

    except:
        logging.error("Fail : 레스토랑 리스트의 요기요 등록 음식점 툴팁을 클릭하지 못했습니다.")
        return False