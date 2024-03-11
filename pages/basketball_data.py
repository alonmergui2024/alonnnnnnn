import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Basketball:
    def __init__(self):
        self.__current_date = datetime.now()
        self.__current_date
        self.__yesterday = self.__current_date - timedelta(days=1)
        self.__current_date = self.__current_date.strftime("%Y%m%d")
        self.__formatted_date = self.__yesterday.strftime("%Y%m%d")
        self.__header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
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


    def get_teamlist(self):
        self.__teams = []
        self.__teams.append("None")
        for self.__item in range(len(self.__table)):
            self.__t = self.__table[self.__item].find_all("td", class_="events__col Table__TD")
            for self.__i in range(len(self.__t)):
                self.__team1 = self.__table[self.__item].find_all("td", class_="events__col Table__TD")[self.__i].text
                if self.__team1 not in self.__teams:
                    self.__teams.append(self.__team1)
                self.__team2 = self.__table[self.__item].find_all("td", class_="colspan__col Table__TD")[self.__i].text.replace("@", "")[4::]
                if self.__team2 not in self.__teams:
                    self.__teams.append(self.__team2)
        return self.__teams
    
    def this_week(self):
        self.__week = []
        for self.__item in range(len(self.__table)):
            self.__t = self.__table[self.__item].find_all("td", class_="events__col Table__TD")
            for self.__i in range(len(self.__t)):
                self.__week.append([self.__table[self.__item].find_all("td", class_="events__col Table__TD")[self.__i].text , self.__table[self.__item].find_all("td", class_="colspan__col Table__TD")[self.__i].text.replace("@", "")[4::] , self.__times[self.__item].text])
        return self.__week
    
    
    def this_week_team(self,team):
        self.__team = team
        self.__week_team = []
        self.__week = self.this_week()
        for self.__item in self.__week:
            if self.__item[0] == self.__team or self.__item[1] == self.__team:
                self.__week_team.append([self.__item[0] , self.__item[1] , self.__item[2]])
        return self.__week_team    


    def rewrite(self,item):
        self.__item = item
        self.__output = ""
        if type(self.__item) == list:
            for self.__g in range(len(self.__item)):
                if len(self.__item[self.__g]) != 3:
                    return "Error: Each item in the list must have exactly 3 elements"
            for self.__i in self.__item:
                self.__output += self.__i[0] + " VS "+ self.__i[1]+ " at " + self.__i[2] + "\n"
            return self.__output
        else:
            return "Error: Input is not a list"

b = Basketball()
print(b.get_teamlist())