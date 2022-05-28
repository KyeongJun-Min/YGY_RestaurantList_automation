from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from data_storage import var_storage as var
from modules import mod_common
from modules import mod_enter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging



def sort_set_rank(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.rank).click()

        logging.info("Pass : 레스토랑 리스트에서 기본 정렬순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 기본 정렬순 정렬을 정상적으로 선택하지 못했습니다.")
        return False



def sort_set_review_avg(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.review_avg).click()

        logging.info("Pass : 레스토랑 리스트에서 별점순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 별점순 정렬을 정상적으로 선택하지 못했습니다.")
        return False



def sort_set_review_count(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.review_count).click()

        logging.info("Pass : 레스토랑 리스트에서 리뷰 많은 순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 리뷰 많은 순 정렬을 정상적으로 선택하지 못했습니다.")
        return False



def sort_set_min_order(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.min_order).click()

        logging.info("Pass : 레스토랑 리스트에서 최소 주문 금액순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 최소 주문 금액순 정렬을 정상적으로 선택하지 못했습니다.")
        return False



def sort_set_distance(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.distance).click()

        logging.info("Pass : 레스토랑 리스트에서 거리순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 거리순 정렬을 정상적으로 선택하지 못했습니다.")
        return False



def sort_set_delivery_time(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        driver.find_element(By.XPATH, xpath.sort.select_box).click()
        driver.find_element(By.XPATH, xpath.sort.delivery_time).click()

        logging.info("Pass : 레스토랑 리스트에서 배달 시간순 정렬을 정상적으로 선택했습니다.")
        return True
    except:
        logging.error("Fail : 레스토랑 리스트에서 배달 시간순 정렬을 정상적으로 선택하지 못했습니다.")
        return False