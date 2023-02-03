from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from loguru import logger

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')