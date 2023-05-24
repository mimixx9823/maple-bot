from logging import log
import requests
from bs4 import BeautifulSoup

def getMapleEventImgUrlList():
    mapleEventUrl = "https://maplestory.nexon.com/News/Event/Ongoing"
    mainResponse = requests.get(mapleEventUrl)
    mainHtml = mainResponse.text

    resultList = list()
    soup = BeautifulSoup(mainHtml, "html.parser")
    for href in soup.find("div", class_="event_board").find_all("dd", class_="data"):
        if href.find("a").text == "썬데이 메이플":
            targetEventUrl = href.find("a")["href"]
            # print(href.find("a").text)
            # print(targetEventUrl)
            # print("https://maplestory.nexon.com" + targetEventUrl)
            targetResponse = requests.get("https://maplestory.nexon.com" + targetEventUrl)
            targetHtml = targetResponse.text
            targetSoup = BeautifulSoup(targetHtml, "html.parser")
            resultList.append(targetSoup.find("div", class_="new_board_con").find("img")["src"])
            break
    return resultList