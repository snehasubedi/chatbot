from datetime import *
import random




import botwork.greeting as c
import time

now = datetime.now()

import requests
from bs4 import BeautifulSoup

import json


class conversation:
    def greeting():
        hour = int(now.hour)
        if hour>=0 and hour<12:
            print("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
        else:
            print("Good evening!")

        print(random.choice(c.greeting))

    def day():
        days = now.strftime("%A, %B %d")
        print(f"Today is {days}")

    def time():
        t=time.localtime()
        current_time=time.strftime("%H:%M:%S",t)
        print(f"The Time is {current_time}")

    


    def weather():
        api_key="196e1b5348ce2de942730aa823c245e9"
        city="Kathmandu"
        base_url='http://api.openweathermap.org/data/2.5/weather?'
        url= f"{base_url}appid={api_key}&q={city}"
        x=requests.get(url)
        y= x.json()
        if y['cod'] != '404':
             main_data=y['main']
             temperature=main_data['temp']-273.15
             print(f"Temperature: {temperature:.2f}°C")
        

    def Exit():
        print(random.choice(c.close))
        exit()

    def news():
        url = 'https://www.bbc.com/news'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        unwanted = ['BBC World News TV', 'BBC World Service Radio',
			'News daily newsletter', 'Mobile app', 'Get in touch']
        for x in list(dict.fromkeys(headlines)):
	         if x.text.strip() not in unwanted:
		            print(x.text.strip())
             
         
