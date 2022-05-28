from functions import func_list



# 테스트 실행부 입니다.
class Test_list:
    def test_17_list_first(self, driver):
        assert func_list.list_count_first(driver) == True

    def test_18_list_scroll(self, driver):
        assert func_list.list_count_scroll(driver) == True



class Test_area:
    def test_19_area_advertisement(self, driver):
        assert func_list.area_exist_advertisement(driver) == True

    def test_20_area_advertisement_tooltip(self, driver):
        assert func_list.area_click_advertisement_tooltip(driver) == True

    def test_21_area_redweek(self, driver):
        assert func_list.area_exist_redweek(driver) == True

    def test_22_area_registered(self, driver):
        assert func_list.area_exist_registered(driver) == True

    def test_23_area_registered_tooltip(self, driver):
        assert func_list.area_click_registered_tooltip(driver) == True
