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
        self.__yesterday = self.__current_date - timedelta(days=1)
        self.__current_date = self.__current_date.strftime("%Y%m%d")
        self.__formatted_date = self.__yesterday.strftime("%Y%m%d")
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
        self.__t = []
        for self.__i in self.__teams:
            self.__t.append(self.__i)
        return self.__t
    
    def this_week(self):
        self.__url = f"https://www.espn.com/nba/schedule/_/date/{self.__formatted_date}"
        self.__url1 = f"https://www.espn.com/nba/schedule/_/date/{self.__current_date}"
        self.__response1 = requests.get(self.__url, headers=self.__header)
        self.__response2 = requests.get(self.__url1, headers=self.__header)
        self.__s1 = BeautifulSoup(self.__response1.content, "html.parser")
        self.__s2 = BeautifulSoup(self.__response2.content, "html.parser")
        self.__results1 = self.__s1.find(id="fittPageContainer")
        self.__results2 = self.__s2.find(id="fittPageContainer")
        self.__table = self.__results1.find_all("tbody", class_="Table__TBODY")
        self.__times = self.__results2.find_all("div", class_="Table__Title")
        self.__week = []
        for self.__item in range(len(self.__table)):
            self.__t = self.__table[self.__item].find_all("td", class_="events__col Table__TD")
            for self.__i in range(len(self.__t)):
                self.__week.append({self.__table[self.__item].find_all("td", class_="events__col Table__TD")[self.__i].text , self.__table[self.__item].find_all("td", class_="colspan__col Table__TD")[self.__i].text.replace("@", "")[4::] , self.__times[self.__item].text})
        return self.__week
    
t = Basketball()
week = t.this_week()
print(week)



