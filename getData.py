import requests
import time
import random
import socket
import http.client
import pymysql
from bs4 import BeautifulSoup

def getData(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body #获取body
    data = body.find('div',{'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date) #添加日期
        inf = day.find_all('p')
        weather = inf[0].string #天气
        temp.append(weather)
        temperature_highest = inf[1].find('span').string #最高温度
        temperature_low = inf[1].find('i').string  # 最低温度
        temp.append(temperature_low)
        temp.append(temperature_highest)
        final.append(temp)
    print('getDate success')
    return final