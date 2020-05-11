from instabot import Bot
import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath

USERNAME = os.environ['INSTAGRAM_USERNAME']
PASSWORD = os.environ['INSTAGRAM_PASSWORD']
DATA_PATH = './instabot'
IMAGES_PATH = os.environ['IMAGES_PATH']


def login():
    bot = Bot(base_path=DATA_PATH)
    bot.login(username=USERNAME, password=PASSWORD)
    return bot


def get_caption(filename):
    return filename.split('.')[0]


def upload():
    bot = login()

    for filename in listdir(IMAGES_PATH):
        filepath = joinpath(IMAGES_PATH, filename)
        if isfile(filepath):
            bot.upload_photo(filepath, caption=get_caption(filename))
