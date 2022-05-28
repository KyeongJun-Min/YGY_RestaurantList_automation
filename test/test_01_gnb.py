from functions import func_gnb


# 테스트 실행부 입니다.
class Test_gnb:
    def test_01_gnb_logo(self, driver):
        assert func_gnb.gnb_enter_logo(driver) == True

    def test_02_gnb_login(self, driver):
        assert func_gnb.gnb_enter_login(driver) == True

    def test_03_gnb_cart(self, driver):
        assert func_gnb.gnb_exist_cart(driver) == True