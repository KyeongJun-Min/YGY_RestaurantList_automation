"""
사용할 url 들을 저장하고 관리합니다.
url 앞부분을 따로 변수화하여 dev, stage 환경에서도 사용 가능하게끔 설계했습니다.
"""

url_REAL = "https://www.yogiyo.co.kr/mobile/#/"

url_TEST = url_REAL


class page:
    service_home = url_TEST
    restaurant_home = url_TEST + "%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C/156091/"
    login = url_TEST + "login/"

class category:
    all = page.restaurant_home
    one = page.restaurant_home + "1%EC%9D%B8%EB%B6%84%EC%A3%BC%EB%AC%B8/"
    franchise = page.restaurant_home + "%ED%94%84%EB%9E%9C%EC%B0%A8%EC%9D%B4%EC%A6%88/"
    chicken = page.restaurant_home + "%EC%B9%98%ED%82%A8/"
    western = page.restaurant_home + "%ED%94%BC%EC%9E%90%EC%96%91%EC%8B%9D/"
    chinese = page.restaurant_home + "%EC%A4%91%EC%8B%9D/"
    korean = page.restaurant_home + "%ED%95%9C%EC%8B%9D/"
    japanese = page.restaurant_home + "%EC%9D%BC%EC%8B%9D%EB%8F%88%EA%B9%8C%EC%8A%A4/"
    pork = page.restaurant_home + "%EC%A1%B1%EB%B0%9C%EB%B3%B4%EC%8C%88/"
    night = page.restaurant_home + "%EC%95%BC%EC%8B%9D/"
    snack = page.restaurant_home + "%EB%B6%84%EC%8B%9D/"
    cafe = page.restaurant_home + "%EC%B9%B4%ED%8E%98%EB%94%94%EC%A0%80%ED%8A%B8/"
    mart = page.restaurant_home + "%ED%8E%B8%EC%9D%98%EC%A0%90/"

