import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import random
import json
import os

class Basketball:
    def __init__(self):
        self.__URL = "https://www.espn.com/nba/teams"
        self.__header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.__response = requests.get(self.__URL, headers=self.__header)
        self.__s = BeautifulSoup(self.__response.content, "html.parser")
        self.__results = self.__s.find(id="fitt-analytics")

        if self.__results:
            self.__team = []
            self.__team.append("None")
            teams = self.__results.find_all('h2', class_='di clr-gray-01 h5')
            for self.__i in teams:
                self.__team.append(self.__i.text)

    def get_teamlist(self):
        for i in self.__team:
            print(i)

base = Basketball()
base.get_teamlist()
