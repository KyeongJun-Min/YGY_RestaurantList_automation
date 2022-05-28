from functions import func_item



# 테스트 실행부 입니다.
class Test_item_info:
    def test_30_item_logo_exist(self, driver):
        assert func_item.item_logo_exist(driver) == True

    def test_31_item_logo_hide(self, driver):
        assert func_item.item_logo_hide(driver) == True

    def test_32_item_logo_total(self, driver):
        assert func_item.item_logo_total(driver) == True

    def test_33_item_name(self, driver):
        assert func_item.item_name(driver) == True

    def test_34_item_review_none(self, driver):
        assert func_item.item_review_none(driver) == True

    def test_35_item_review_exist(self, driver):
        assert func_item.item_review_exist(driver) == True

    def test_36_item_review_total(self, driver):
        assert func_item.item_review_total(driver) == True

    def test_37_item_reply_none(self, driver):
        assert func_item.item_reply_none(driver) == True

    def test_38_item_reply_exist(self, driver):
        assert func_item.item_reply_exist(driver) == True

    def test_39_item_reply_total(self, driver):
        assert func_item.item_reply_total(driver) == True

    def test_40_item_yogiseo_payment(self, driver):
        assert func_item.item_yogiseo_payment(driver) == True

    def test_41_item_min_price(self, driver):
        assert func_item.item_min_price(driver) == True

    def test_42_item_delivery_time(self, driver):
        assert func_item.item_delivery_time(driver) == True

    def test_43_item_badge_flatRate(self, driver):
        assert func_item.item_badge_flatRate(driver) == True

    def test_44_item_badge_fixedRate(self, driver):
        assert func_item.item_badge_fixedRate(driver) == True

    def test_45_item_badge_cesco(self, driver):
        assert func_item.item_badge_cesco(driver) == True


class Test_item_click:
    def test_46_item_enter_restaurant(self, driver):
        assert func_item.item_enter_restaurant_end(driver) == True