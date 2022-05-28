from data_storage import url_storage as url
from data_storage import xpath_storage as xpath
from data_storage import var_storage as var
from modules import mod_common
from modules import mod_enter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging



def item_logo_exist(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)

        if(mod_common.is_element_exist(driver, xpath.item.logos) == True):
            logging.info("Pass : 레스토랑 로고 이미지가 노출되고 있습니다.")
            return True
        else:
            raise Exception("레스토랑 로고 이미지 노출 에러")
    except:
        logging.error("Fail : 레스토랑 로고 이미지가 노출되지 않고있습니다.")
        return False



def item_logo_hide(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        if(mod_common.is_element_exist(driver, xpath.item.logos_hided) == True):
            logging.info("Pass : 서비스 미제공 로고 이미지가 노출되고 있습니다.")
            return True
        else:
            raise Exception("서비스 미제공 로고 이미지 노출 에러")
    except:
        logging.error("Fail : 서비스 미제공 로고 이미지가 노출되지 않고있습니다.")
        return False


def item_logo_total(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        count_logo = driver.find_elements(By.XPATH, xpath.item.logos).__len__()
        count_logo_hided = driver.find_elements(By.XPATH, xpath.item.logos_hided).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if((count_logo + count_logo_hided) == count_total_items):
            logging.info("Pass : 전체 레스토랑 항목들에서 레스토랑/서비스 미제공 로고 이미지가 노출 중입니다.")
            return True
        else:
            raise Exception("전체 로고 이미지 노출 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 로고 이미지가 노출되지 않는 항목이 존재합니다.")
        return False



def item_name(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        count_name = driver.find_elements(By.XPATH, xpath.item.names).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if(count_name == count_total_items and mod_common.is_element_exist(driver, xpath.item.names)):
            logging.info("Pass : 전체 레스토랑 항목들에서 가게명이 노출 중입니다.")
            return True
        else:
            raise Exception("전체 가게명 노출 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 가게명이 노출되지 않는 항목이 존재합니다.")
        return False



def item_review_none(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        if(mod_common.is_element_exist(driver, xpath.item.stars_hided) == True and mod_common.is_element_exist(driver, xpath.item.reviews_hided) == True):
            logging.info("Pass : 별점/리뷰가 존재하지 않는 레스토랑이 정상적으로 노출 중입니다.")
            return True
        else:
            raise Exception("별점/리뷰 없는 항목 에러")
    except:
        logging.error("Fail : 별점/리뷰가 존재하지 않는 레스토랑이 정상적으로 노출되지 않습니다.")
        return False




def item_review_exist(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        if(mod_common.is_element_exist(driver, xpath.item.stars) == True and mod_common.is_element_exist(driver, xpath.item.reviews) == True):
            logging.info("Pass : 별점/리뷰가 존재하는 레스토랑이 정상적으로 노출 중입니다.")
            return True
        else:
            raise Exception("별점/리뷰 있는 항목 에러")
    except:
        logging.error("Fail : 별점/리뷰가 존재하는 레스토랑이 정상적으로 노출되지 않습니다.")
        return False



def item_review_total(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        count_review = driver.find_elements(By.XPATH, xpath.item.reviews).__len__()
        count_review_hided = driver.find_elements(By.XPATH, xpath.item.reviews_hided).__len__()

        count_star = driver.find_elements(By.XPATH, xpath.item.stars).__len__()
        count_star_hided = driver.find_elements(By.XPATH, xpath.item.stars_hided).__len__()

        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if((count_review == count_star) and (count_review_hided == count_star_hided) and ((count_review_hided + count_review) == count_total_items)):
            logging.info("별점 있는 항목 수와 리뷰 있는 항목 수가 동일합니다.")
            logging.info("별점 없는 항목 수와 리뷰 없는 항목 수가 동일합니다.")
            logging.info("Pass : 별점/리뷰 없는 항목과 별점/리뷰 있는 항목의 총합이 전체 레스토랑 항목 수와 동일합니다.")
            return True
        else:
            raise Exception("별점/리뷰 없는 항목과 별점/리뷰 있는 항목의 총합 에러")
    except:
        logging.error("Fail : 별점/리뷰 없는 항목과 별점/리뷰 있는 항목의 총합이 전체 레스토랑 항목 수와 일치하지 않습니다.")
        return False



def item_reply_none(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        if(mod_common.is_element_exist(driver, xpath.item.replies_hided) == True):
            logging.info("Pass : 사장님 댓글이 존재하지 않는 항목들이 정상적으로 노출되고 있습니다.")
            return True
        else:
            raise Exception("사장님 댓글 미노출 에러")
    except:
        logging.error("Fail : 사장님 댓글이 존재하지 않는 항목들이 정상적으로 노출되지 않습니다.")
        return False




def item_reply_exist(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        if(mod_common.is_element_exist(driver, xpath.item.replies) == True):
            logging.info("Pass : 사장님 댓글이 존재하는 항목들이 정상적으로 노출되고 있습니다.")
            return True
        else:
            raise Exception("사장님 댓글 노출 에러")
    except:
        logging.error("Fail : 사장님 댓글이 존재하는 항목들이 정상적으로 노출되지 않습니다.")
        return False



def item_reply_total(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_until_end(driver)

        count_reply = driver.find_elements(By.XPATH, xpath.item.replies).__len__()
        count_reply_hided = driver.find_elements(By.XPATH, xpath.item.replies_hided).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if((count_reply + count_reply_hided) == count_total_items):
            logging.info("Pass : 전체 레스토랑 항목들에서 사장님 댓글 영역 있음/없음이 정상적으로 노출 중입니다.")
            return True
        else:
            raise Exception("전체 사장님 댓글 수 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 사장님 댓글 영역 있음/없음이 정상적으로 노출되지 않습니다.")
        return False



def item_yogiseo_payment(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        count_payment = driver.find_elements(By.XPATH, xpath.item.yogiseo_payments).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if (count_payment == count_total_items and mod_common.is_element_exist(driver, xpath.item.yogiseo_payments)):
            logging.info("Pass : 전체 레스토랑 항목들에서 요기서결제가 노출 중입니다.")
            return True
        else:
            raise Exception("전체 항목들 요기서결제 노출 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 요기서결제가 노출되지 않는 항목이 존재합니다.")
        return False



def item_min_price(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        count_min = driver.find_elements(By.XPATH, xpath.item.min_prices).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if (count_min == count_total_items and mod_common.is_element_exist(driver, xpath.item.min_prices)):
            logging.info("Pass : 전체 레스토랑 항목들에서 배달 최소 금액이 노출 중입니다.")
            return True
        else:
            raise Exception("전체 항목들 배달 최소 금액 노출 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 배달 최소 금액이 노출되지 않는 항목이 존재합니다.")
        return False



def item_delivery_time(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        count_delivery = driver.find_elements(By.XPATH, xpath.item.delivery_times).__len__()
        count_total_items = driver.find_elements(By.XPATH, xpath.item.items).__len__()

        if (count_delivery == count_total_items and mod_common.is_element_exist(driver, xpath.item.delivery_times)):
            logging.info("Pass : 전체 레스토랑 항목들에서 배달 시간이 노출 중입니다.")
            return True
        else:
            raise Exception("전체 항목들 배달 시간 노출 에러")
    except:
        logging.error("Fail : 전체 레스토랑 항목들에서 배달 시간이 노출되지 않는 항목이 존재합니다.")
        return False


def item_badge_flatRate(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        if(mod_common.is_element_exist(driver, xpath.item.badge_flatRates) == True):
            logging.info("Pass : 정액 할인 뱃지가 노출되고 있습니다.")
            return True
        else:
            raise Exception("정액 할인 뱃지 노출 에러")
    except:
        logging.error("Fail : 정액 할인 뱃지가 노출되지 않고있습니다.")
        return False



def item_badge_fixedRate(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        if(mod_common.is_element_exist(driver, xpath.item.badge_fixedRates) == True):
            logging.info("Pass : 정률 할인 뱃지가 노출되고 있습니다.")
            return True
        else:
            raise Exception("정률 할인 뱃지 노출 에러")
    except:
        logging.error("Fail : 정률 할인 뱃지가 노출되지 않고있습니다.")
        return False
    
    
    
def item_badge_cesco(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        mod_common.scroll_down_fast(driver)

        if(mod_common.is_element_exist(driver, xpath.item.badge_cescos) == True):
            logging.info("Pass : 세스코 뱃지가 노출되고 있습니다.")
            return True
        else:
            raise Exception("세스코 뱃지 노출 에러")
    except:
        logging.error("Fail : 세스코 뱃지가 노출되지 않고있습니다.")
        return False



def item_enter_restaurant_end(driver):
    try:
        mod_enter.enter_restaurant_list(driver, var.address)
        name_list = driver.find_elements(By.XPATH, xpath.item.names)
        title_in_list = name_list[0].text

        name_list[0].click()
        sleep(2)
        end = driver.find_element(By.XPATH, xpath.item.restaurant_end_title)
        end_title = end.text

        if(title_in_list == end_title):
            logging.info("Pass : 레스토랑 리스트에서 항목을 클릭하여 해당 레스토랑 엔드로 정상적으로 이동했습니다.")
            return True
        else:
            raise Exception("레스토랑 엔드 진입 에러")
    except:
        logging.error("Fail : 레스토랑 리스트에서 항목을 클릭하여 해당 레스토랑 엔드로 정상 진입하지 못했습니다.")
        return False
