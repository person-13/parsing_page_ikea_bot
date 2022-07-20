import json
import requests
import time

from bs4 import BeautifulSoup
from IPython.display import clear_output
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

TOKEN = 'ТОКЕН ВАШЕГО БОТА'

def add_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0' +
        '(Windows NT 10.0; Win64; x64)' + 
        'AppleWebKit/537.36 (KHTML, like Gecko)' + 
        'Chrome/79.0.3945.79 Safari/537.36'
    )
    
    return options

def install_chrome_driver():
    
    return ChromeDriverManager().install()

def open_page(url):
    options = add_chrome_options()
    install_driver = install_chrome_driver()
    
    driver = webdriver.Chrome(
        install_driver, 
        chrome_options=options
    )
    driver.get(url)
    
    return driver

def get_ikea_html(url, driver):
    page_source = driver.page_source
    
    return page_source

def get_h1(page_source):
    soup = BeautifulSoup(page_source, 'lxml')
    html_h1 = soup.find_all('h1')

    return html_h1

def get_chat_id(token):
    r = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    answer = json.loads(r.text)
    chat_id = answer['result'][-1]['message']['chat']['id']
    
    return chat_id

def post_message(token, id_chat, message):
    params = {
        'chat_id' : chat_id,
        'text' : message
    }
    requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        data = params
    )

URL = 'https://www.ikea.com/ru/ru/'
start_page_ikea_h1 = 'ИКЕА - официальный интернет-магазин мебели '

start_h1 = (-1)
driver = open_page(URL)

cnt = 0

while start_h1 != start_page_ikea_h1:
    page_source = get_ikea_html(URL, driver)
    start_h1 = get_h1(page_source)[0].text
    print(start_h1)
    time.sleep(0.5)
    driver.refresh()
    
    if cnt%100 == 0:
        clear_output(wait=False)
    cnt += 1
    
chat_id = get_chat_id(TOKEN)
message = 'ГЛАВНАЯ СТРАНИЦА ОТКРЫТА'
post_message(TOKEN, chat_id, message)