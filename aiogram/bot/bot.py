import logging
from json import loads

import requests
from aiogram import Bot, Dispatcher, executor, types
from data_base import sqlite_db

API_TOKEN = '2063505505:AAFBOL9l7sEumsjUHKPDXy8ck1fqdZH0zjQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def start_bot():
    print('Bot online')
    sqlite_db.start_db()


def start_get_all(value):
    art = value.text.split(" ")[1]
    response = requests.get(f'https://wbx-content-v2.wbstatic.net/other-sellers/{art}.json?locale=ru').text
    if len(response[1:-1].split(", ")) > 1:
        p_id = ";".join([str(i) for i in response[1:-1].split(", ")])
    else:
        p_id = response[1:-1]
    response_json = requests.get(f'https://wbxcatalog-ru.wildberries.ru/nm-2-card/catalog?locale=ru&nm={p_id}').text
    brand = (loads(response_json).get("data").get("products")[0].get("brand"))
    title = (loads(response_json).get("data").get("products")[0].get("name"))
    sqlite_db.start_db()
    sqlite_db.sql_add_brand_and_title(title, brand)
    return title, brand


@dp.message_handler(commands='get_brand')
async def start_get_brand(message: types.Message):
    json_asw = start_get_all(message)
    try:
        await message.answer(json_asw[1])
    except IndexError:
        await message.answer('Продукции с таким артикулом не существует')

    # response = requests.get(f'https://www.wildberries.ru/catalog/{art}/detail.aspx?targetUrl=XS').text
    # try:
    #     json_data = re.findall(r'var google_tag_params = ({[\d\D]+?});\s', response)[0]


@dp.message_handler(commands='get_title')
async def start_get_title(message: types.Message):
    json_asw = start_get_all(message)
    try:
        await message.answer(json_asw[0])
    except IndexError:
        await message.answer('Продукции с таким артикулом не существует')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # response = requests.get(f'https://www.wildberries.ru/catalog/{art}/detail.aspx?targetUrl=XS').text
    # print(response)
    # try:
    #     json_data = re.findall(r'var google_tag_params = ({[\d\D]+?});\s', response)[0]
    #     await message.answer(loads(json_data).get("Ptype")[0])
    # except IndexError:
    #     await message.answer('Продукции с таким артикулом не существует')

# @dp.message_handler(commands='get_all')
# async def start_get_brand(message: types.Message):
#     art = message.text.split(" ")[1]
#     response = requests.get(f'https://wbx-content-v2.wbstatic.net/other-sellers/{art}.json?locale=ru').text
#     response_json = requests.get(f'https://wbxcatalog-ru.wildberries.ru/nm-2-card/catalog?locale=ru&nm=\
#     {";".join([str(i) for i in response[1:-1].split(", ")])}').text
#     print(response_json)
#     print(loads(response_json))
#     json_asw = (loads(response_json).get("data"))
#     print(json_asw)


    