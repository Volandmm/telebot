from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv('template.env')
API_KEY = os.getenv('API_KEY')
if API_KEY is None:
    exit('BOT_TOKEN отсутствует в переменных окружения')
BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    exit('BOT_TOKEN отсутствует в переменных окружения')
API_BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'
DEFAULT_LANG = 'ru-en'
