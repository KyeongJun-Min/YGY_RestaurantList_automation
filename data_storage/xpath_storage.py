"""
영역별로 해당 영역에서 사용하는 xpath 값들을 정리했습니다.
find_elements로 여러개의 elements들을 찾아야하는 xpath 값들의 끝에는 s를 붙였습니다.
::tag명 형태를 활용하여 기준점으로부터 xpath 값을 잡는 방법도 사용했습니다.
"""


class search:
    input = "//input[@name='address_input']"
    searching_button = "//button[@class='btn btn-default ico-pick']"



class gnb:
    logo = "//h1[@class='logo pull-left']"
    login_btn = "//button[@class='btn btn-login ng-binding']"
    cart_btn = "//button[@class='btn btn-warning hidden-xs ng-binding']"



class category:
    tabs = "//span[@class='category-name ng-binding']/parent::li"


class list:
    items = "//div[@class='item clearfix']"

    advertisement_area = "//p[text()='우리동네 플러스']"
    advertisement_btn = "//button[@id='adtooltip']"
    redweek_area = "//p[text()='슈퍼레드위크 추천']"
    registered_area = "//p[text()='요기요 등록 음식점']"
    registered_btn = "//button[@id='ranktooltip']"


class sort:
    select_box = "//div[@class='list-option-inner']/select"
    rank = "//option[@value='rank']"
    review_avg = "//option[@value='review_avg']"
    review_count = "//option[@value='review_count']"
    min_order = "//option[@value='min_order_value']"
    distance = "//option[@value='distance']"
    delivery_time = "//option[@value='estimated_delivery_time']"


class item:
    items = "//div[@class='item clearfix']"
    logos = "//div[@class='logo']"
    logos_hided = "//div[@class='logo ng-hide']"
    names = "//div[@class='restaurant-name ng-binding']"
    stars = "//span[@class='ico-star1 ng-binding']"
    stars_hided = "//span[@class='ico-star1 ng-binding ng-hide']"
    reviews = "//span[@class='review_num ng-binding' and @ng-show='restaurant.review_count > 0']"
    reviews_hided = "//span[@class='review_num ng-binding ng-hide' and @ng-show='restaurant.review_count > 0']"

    replies = "//span[@class='review_num ng-binding' and @ng-show='restaurant.owner_reply_count > 0']"
    replies_hided = "//span[@class='review_num ng-binding ng-hide' and @ng-show='restaurant.owner_reply_count > 0']"
    yogiseo_payments = "//li[@class='payment-methods ng-binding yogiseo-payment']"
    min_prices = "//li[@class='min-price ng-binding']"
    delivery_times = "//li[@class='delivery-time ng-binding']"
    badge_flatRates = "//span[@class='coupon-base ng-binding']"
    badge_fixedRates = "//span[@class='coupon-base coupon-style1 ng-binding']"
    badge_cescos = "//span[@class='ico-cesco']"

    restaurant_end_title = "//span[@class='restaurant-name ng-binding']"

