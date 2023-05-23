from logging import log
import requests
from bs4 import BeautifulSoup

mapleEventUrl = "https://maplestory.nexon.com/News/Event/Ongoing"
response = requests.get(mapleEventUrl)
html = response.text

soup = BeautifulSoup(html, "html.parser")
for href in soup.find("div", class_="event_board").find_all("dd", class_="data"):
    print(href.find("a").text)
    print(href.find("a")["href"])
