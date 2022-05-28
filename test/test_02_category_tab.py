from functions import func_category_tab



# 테스트 실행부 입니다.
class Test_category_tab:
    def test_04_category_all(self, driver):
        assert func_category_tab.category_enter_all(driver) == True

    def test_05_category_one(self, driver):
        assert func_category_tab.category_enter_one(driver) == True

    def test_06_category_fanchise(self, driver):
        assert func_category_tab.category_enter_franchise(driver) == True

    def test_07_category_chicken(self, driver):
        assert func_category_tab.category_enter_chicken(driver) == True

    def test_08_category_western(self, driver):
        assert func_category_tab.category_enter_western(driver) == True

    def test_09_category_chinese(self, driver):
        assert func_category_tab.category_enter_chinese(driver) == True

    def test_10_category_korean(self, driver):
        assert func_category_tab.category_enter_korean(driver) == True

    def test_11_category_japanese(self, driver):
        assert func_category_tab.category_enter_japanese(driver) == True

    def test_12_category_pork(self, driver):
        assert func_category_tab.category_enter_pork(driver) == True

    def test_13_category_night(self, driver):
        assert func_category_tab.category_enter_night(driver) == True

    def test_14_category_snack(self, driver):
        assert func_category_tab.category_enter_snack(driver) == True

    def test_15_category_cafe(self, driver):
        assert func_category_tab.category_enter_cafe(driver) == True

    def test_16_category_mart(self, driver):
        assert func_category_tab.category_enter_mart(driver) == True