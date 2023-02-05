from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logger as logg

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start program.')
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!''Calculator welcomes you!\n')
    await update.message.reply_text(f'Put "0" to start Main menu:\n')

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start main menu.')
    await update.message.reply_text(f'Would you like working with:\n'
                'a - rational\n'
                # 'b - complex\n' 
                'b - exit?\n')

async def racional_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start menu with rational.')
    await update.message.reply_text(f'Select operation and put two numbers by ENTER:\n'
            '1 - sum\n'
            '2 - subtraction\n'
            '3 - multiplication\n'
            '4 - division\n'
            '5 - exponentiation\n'
            '6 - square root - enter one number\n'
            '0 - main menu') 

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation sum')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation sub')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation mult')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def div_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start menu division.')
    await update.message.reply_text(f'Select division and put two numbers by ENTER::\n'
            'd - /\n'
            'dc - //\n'
            'do - %\n'
            'a - operating menu')

async def div1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation div')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if y != 0:
        await update.message.reply_text(f'{x} / {y} = {x/y}')
    else:
        await update.message.reply_text(f'Error: Cannot be divided by 0 (zero)!') 
        logg.logging.warning("Incorrect data entered: '0'!")

async def div2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation div2')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} // {y} = {x//y}')

async def div3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation div3')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} % {y} = {x%y}')

async def pow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation pow')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ** {y} = {x**y}')

async def sqrt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Start operation sqrt')
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    await update.message.reply_text(f'{x} ** 0.5 = {x**0.5}')

async def exit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logg.logging.info('Stop program')
    await update.message.reply_text(f'Stop program. See you soon, {update.effective_user.first_name}!')
  
