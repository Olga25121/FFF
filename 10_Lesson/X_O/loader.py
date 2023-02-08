from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from loguru import logger

bot = Bot('6094800431:AAHsQrlQ5yXc6ujSezQH2phYksewKfAn2Ys')
dp = Dispatcher(bot)  # обработчик

logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')
