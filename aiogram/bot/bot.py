import logging
import re
from json import loads

import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2063505505:AAFBOL9l7sEumsjUHKPDXy8ck1fqdZH0zjQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='get_brand')
async def start_get_brand(message: types.Message):
    art = message.text.split(" ")[1]
    response = requests.get(f'https://www.wildberries.ru/catalog/{art}/detail.aspx?targetUrl=XS').text
    try:
        json_data = re.findall(r'var google_tag_params = ({[\d\D]+?});\s', response)[0]
        await message.answer(loads(json_data).get("Pbrand"))
    except IndexError:
        await message.answer('Продукции с таким артикулом не существует')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    