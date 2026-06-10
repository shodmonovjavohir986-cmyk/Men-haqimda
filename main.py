import asyncio 
import logging

from aiogram import Bot, Dispatcher
from keyboards import inline_router
from handlers import Men_haqimda_handler

API_TOKEN = "7559356998:AAEncUsqUKnO3wAJJj6MOVAyAOhyQ7-pkDQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()



async def main():
   dp.include_router(inline_router)
   dp.include_router(Men_haqimda_handler)
   await dp.start_polling(bot)

if __name__ == "__main__":
   try:
       logging.basicConfig(level=logging.INFO)
       asyncio.run(main())
   except KeyboardInterrupt:
     print("Bot ishladi")