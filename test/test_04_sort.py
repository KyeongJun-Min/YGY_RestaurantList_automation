from functions import func_sort



# 테스트 실행부 입니다.
class Test_sort:
    def test_24_sort_rank(self, driver):
        assert func_sort.sort_set_rank(driver) == True

    def test_25_sort_review_avg(self, driver):
        assert func_sort.sort_set_review_avg(driver) == True

    def test_26_sort_review_count(self, driver):
        assert func_sort.sort_set_review_count(driver) == True

    def test_27_sort_min_order(self, driver):
        assert func_sort.sort_set_min_order(driver) == True

    def test_28_sort_distance(self, driver):
        assert func_sort.sort_set_distance(driver) == True

    def test_29_sort_delivery_time(self, driver):
        assert func_sort.sort_set_delivery_time(driver) == True