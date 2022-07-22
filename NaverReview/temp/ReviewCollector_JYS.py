from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class ReviewCollector:
    def __init__(self):
        self.open_browser()
        self.collect_res_info("https://www.mangoplate.com/restaurants/eLq_Q72bscee")
        self.collect_res_reviews()


    def open_browser(self):
        path = "c:/python/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(3)
        url = "https://www.mangoplate.com/restaurants/1KoxMlQL0NZk"
        self.driver.get(url)
        time.sleep(5)

    def collect_data(self):
        # 백인준 (합칠거)
        print()



    # 1. 맛집 베스트 XX곳 목록 정보 가져오기
    # 1) 수집할 데이터: 타이틀, 타이틀링크
    # 2) 목표데이터: 300개
    # 3) 목적: 수집한 데이터를 2번 함수에 제공
    # 4) 가공 형태
    # -> link_list = {"타이틀1":"링크주소", "타이틀2":"링크주소", "타이틀3":"링크주소" ...}
    def collect_theme_list(self):
        # 유승하
        print()

    # 2. 맛집리스트 별 식당정보 가져오기
    # 1) 수집할 데이터: 식당목록, 식당상세페이지 링크, 사진(식당이름+.jpg)
    # 2) 요구사항: 사진은 xx 맛집 베스트 폴더안에 저장
    # 3) 목적: 식당목록, 식당상세페이지 링크를 3번 함수에 제공
    # 4) 가공 형태
    # -> res_list = {"식당이름1":"링크주소", "식당이름2":"링크주소", "식당이름3":"링크주소" ...}
    def collect_res_list(self):
        # 박종원
        # for title, link in link_list.items():
        #     print(title, link)
        #     driver.get(link)
        print()

    # 3. 식당 별 정보 가져오기
    # 1) 수집할 데이터: 식당이름, 주소, 전화번호, 음식 종류, 가격대, 메뉴, 메뉴가격
    # 2) 가공 형태
    # -> info_list = {"식당이름":[별점, 별점개수, 주소, 전화번호, 음식종류, 가격대], ...}
    # -> menu_list = {"식당이름":{"메뉴1":가격(int), "메뉴2":가격(int), "메뉴3":가격(int)}, ...]}
    def collect_res_info(self, url):
        # 권기민
        self.driver.get(url)
        title = self.driver.find_element(By.CSS_SELECTOR, '.restaurant_name') #식당이름
        star_rivew = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/strong')
        evaluation = self.driver.find_element(By.CSS_SELECTOR, '.cnt.favorite')
        info = self.driver.find_element(By.XPATH,'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td')
        index = info.text.index('지')
        #print(info.text[0:index-1])
        telephone_number = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td')
        price_range = self.driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[4]/td')
        
        try:
            time.sleep(3)
            meun = self.driver.find_element(By.CLASS_NAME, 'menu_td')
            if meun.text != None:
                print(meun.text)
            else:
                pass
        except NoSuchElementException as ns:
            print("메뉴가 없습니다.")
        
        menulist = meun.find_elements(By.CLASS_NAME, "Restaurant_Menu")
        pricelist = meun.find_elements(By.CLASS_NAME, "Restaurant_MenuPrice")
        #print(len(menulist))
        lista = []
        for x in menulist:
            #print(x.text)
            lista.append(x.text)
        listb = []
        for y in pricelist:
            a = y.text.replace(',','')
            b = a.replace('원','')
            listb.append(b)
        print(listb) 
        
        title1 = title.text
        dic= {title1:{}}
        for x in range(0, len(lista)):
            k = lista[x]
            v = listb[x]
            dic[title1][k] = v
        print(dic)
        
        infolist = ["별점: "+star_rivew.text+"","별점갯수: "+evaluation.text+"","주소: "+info.text[0:index-1]+"","전화번호:"+telephone_number.text+"","가격대:"+str(price_range.text)+""]
        #print(infolist)
        info_list = {title.text:infolist}
        print(info_list)
        '''
        for title, link in res_list.items():
            #print(title, link)
            self.driver.get(link)
            info_list = {title.text:infolist}
            print(info_list)
            #menu_list = [title]=(f"{}{}")
        '''
        print()

    # 4. 식당 별 리뷰정보 가져오기
    # 1) 수집할 데이터: 식당이름, 리뷰갯수, (갯수)맛있다, 괜찮다, 별로, 리뷰내용
    # 2) 가공 형태
    # -> review_list = {"식당이름", [리뷰갯수(int), 맛있다(int), 괜찮다(int), 별로(int), [리뷰내용(str)]]}
    
    def collect_res_reviews(self):
        # 지예성
        restaurantname = self.driver.find_element(By.CLASS_NAME,"restaurant_name").text
        print(restaurantname)

        self.driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(2) > button").send_keys(Keys.ENTER)
        oldcountB, newcountB = None, 0
        # 더보기 클릭
        while True:
            try:
                # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
                if oldcountB == newcountB:
                    print("old:", oldcountB, "new:", newcountB)
                    break
                else:
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    oldcountB = len(reviews)
                    print("old:", oldcountB)
                    btn = self.driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(1)
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    newcountB = len(reviews)
                    print("new:", newcountB)
                    print()
            except:
                break

        self.driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(3) > button").send_keys(Keys.ENTER)
        oldcountC, newcountC = None, 0
        # 더보기 클릭
        while True:
            try:
                # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
                if oldcountC == newcountC:
                    print("old:", oldcountC, "new:", newcountC)
                    break
                else:
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    oldcountC = len(reviews)
                    print("old:", oldcountC)
                    btn = self.driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(1)
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    newcountC = len(reviews)
                    print("new:", newcountC)
                    print()
            except:
                break

        self.driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(4) > button").send_keys(Keys.ENTER)
        oldcountD, newcountD = None, 0
        # 더보기 클릭
        while True:
            try:
                # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
                if oldcountD == newcountD:
                    print("old:", oldcountD, "new:", newcountD)
                    break
                else:
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    oldcountD = len(reviews)
                    print("old:", oldcountD)
                    btn = self.driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(1)
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    newcountD = len(reviews)
                    print("new:", newcountD)
                    print()
            except:
                break
        self.driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > header > ul > li:nth-child(1) > button").send_keys(Keys.ENTER)
        oldcountA, newcountA = None, 0
        # 더보기 클릭
        while True:
            try:
                # 더보기 버튼 클릭 전 리뷰 갯수와 클릭 후 리뷰 갯수를 비교하여 두 값이 동일할 경우 버튼 클릭을 멈춤
                if oldcountA == newcountA:
                    print("old:", oldcountA, "new:", newcountA)
                    break
                else:
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    oldcountA = len(reviews)
                    print("old:", oldcountA)
                    btn = self.driver.find_element(By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(1)
                    reviews = self.driver.find_elements(By.CLASS_NAME, "RestaurantReviewItem__ReviewText")
                    newcountA = len(reviews)
                    print("new:", newcountA)
                    print()
            except:
                break
        time.sleep(2)
        i = 1
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, "body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > ul > li:nth-child("+str(i)+") > a").send_keys(Keys.ENTER) #댓글 클릭
                time.sleep(2)
                self.driver.window_handles[0]
                self.driver.switch_to.window(self.driver.window_handles[1])
                name = self.driver.find_element(By.CLASS_NAME,"ReviewCard__UserName").text
                comment = self.driver.find_element(By.CLASS_NAME,"ReviewCard__ReviewText").text
                print("닉네임: ", name, "\n")
                print(comment, "\n")
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                i += 1
            except:
                break
<<<<<<< HEAD
        reviewlist = ["전체: ", newcountA, "맛있다: ", newcountB, "괜찮다: ", newcountC, "별로다: ", newcountD, ["닉네임: ", name, "리뷰: ", comment]]
        review_list = {restaurantname : reviewlist}
        print(review_list)
#    print(review_list)
rc = ReviewCollector()
=======

    def connect_db(self):
        print()

if __name__ == "__main__":
    ReviewCollector()
>>>>>>> f4a9c28f2984a7f30e5fa6c15f399613c67ac598
