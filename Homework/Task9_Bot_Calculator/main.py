from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logger as logg
from bot_command import *

app = ApplicationBuilder().token("").build()


app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("0", main_menu))
app.add_handler(CommandHandler("a", racional_menu))
app.add_handler(CommandHandler("1", sum))
app.add_handler(CommandHandler("2", sub))
app.add_handler(CommandHandler("3", mult))
app.add_handler(CommandHandler("4", div_menu))
app.add_handler(CommandHandler("d", div1))
app.add_handler(CommandHandler("dc", div2))
app.add_handler(CommandHandler("do", div3))
app.add_handler(CommandHandler("5", pow))
app.add_handler(CommandHandler("6", sqrt))
app.add_handler(CommandHandler("b", exit_menu))


print('start')
app.run_polling()