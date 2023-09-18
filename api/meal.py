import requests
from bs4 import BeautifulSoup


def meal1():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blBI&pkid=682&os=24929829&qvt=0&query=%ED%8F%AC%EC%82%B0%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90%20%EA%B8%89%EC%8B%9D%EC%8B%9D%EB%8B%A8"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    급식데이터 = soup.find_all("div", {"class": "time_normal_list"})
    날짜데이터 = soup.find_all("strong", {"class": "cm_date"})

    날짜리스트 = []

    for cm_date in 날짜데이터:
        if cm_date.get_text() not in 날짜리스트:
            날짜리스트.append(cm_date.get_text())

    if 날짜리스트 == []:
        print("오늘은 쉬는 날입니다.")
    else:
        today_now = []

        time = 0

        for i in 날짜리스트:
            if "TODAY" in i:
                break
            else:
                time = time + 1

        급식리스트 = []

        for time_normal_list in 급식데이터:
            if time_normal_list.get_text() not in 급식리스트:
                급식리스트.append(time_normal_list.get_text())

        result_list = []
        if 날짜리스트 == []:
            result_list.append("오늘은 쉬는 날입니다.")
        else:
            result_list.append(list(map(str, 급식리스트[time].split())))  # 조식
            result_list.append(list(map(str, 급식리스트[time + 1].split())))  # 중식
            result_list.append(list(map(str, 급식리스트[time + 2].split())))  # 석식
    return result_list


if __name__ == "__main__":
    a = meal1()
    print(meal1())
