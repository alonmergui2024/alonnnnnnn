import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class Basketball:
    def __init__(self):
        
        self.__URL = "https://www.espn.com/nba/teams"
        self.__header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.__current_date = datetime.now()
        self.__formatted_date = self.__current_date.strftime("%Y%m%d")
        self.__response = requests.get(self.__URL, headers=self.__header)
        self.__s = BeautifulSoup(self.__response.content, "html.parser")
        self.__results = self.__s.find(id="fitt-analytics")
        

        if self.__results:
            self.__teams = []
            self.__teams.append("None")
            teamss = self.__results.find_all('h2', class_='di clr-gray-01 h5')
            for self.__i in teamss:
                self.__teams.append(self.__i.text)

    def get_teamlist(self):
        for i in self.__teams:
            print(i)
    
    def this_week(self,team):
        self.__team = team
        self.__week = []
        self.__url = f"https://www.espn.com/nba/schedule/_/date/{self.__formatted_date}"
        self.__response1 = requests.get(self.__url, headers=self.__header)
        self.__s1 = BeautifulSoup(self.__response1.content, "html.parser")
        self.__results1 = self.__s1.find(id="fittPageContainer")
        self.__table = self.__results1.find_all("div", class_="ScheduleTables mb5 ScheduleTables--nba ScheduleTables--basketball")
        self.__teams1 = self.__results1.find_all("td", class_="events__col Table__TD")
        self.__teams2 = self.__results1.find_all("td", class_="colspan__col Table__TD")
        self.__times = self.__results1.find_all("td", class_="date__col Table__TD")
        self.__games = list(zip(self.__teams1, self.__teams2, self.__times))
        for self.__x, self.__y, self.__z in self.__games:
            self.__time = self.__z.text.strip()
            self.__g = (f'{self.__x.text}{self.__y.text} {self.__time}').replace('@', 'vs')
            print(self.__g)


header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
formatted_date = current_date.strftime("%Y%m%d")
url = f"https://www.espn.com/nba/schedule/_/date/{formatted_date}"
response1 = requests.get(url, headers=header)
s1 = BeautifulSoup(response1.content, "html.parser")
results1 = s1.find(id="fittPageContainer")
table = results1.find_all("tbody", class_="Table__TBODY")
times = results1.find_all("div", class_="Table__Title")
t = table[0].find_all("td", class_="events__col Table__TD")
week = []
for i in range(len(table)):
    print(times[i].text)
#for i in range(len(week)):
#    print(week[i])
for i in range(len(t)):
    print(table[0].find_all("td", class_="events__col Table__TD")[i].text + " VS "+ table[0].find_all("td", class_="colspan__col Table__TD")[i].text.replace("@", "")[4::])
