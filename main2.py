from aiogram import Dispatcher, Bot, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot:Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, что бы звпустить бота'),
        types.BotCommand(command='/help', description='Команда для того,чтобы узнать,с чем может помошь наш бот')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, ты в основной конфигурации бота скупщика')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Данный бот может с легкостью выкупить твой аккаунт')

@dp.message_handler(commands='about')
async def about(message: types.Message):
    await message.reply('Бот приспособлен выдавать самые лучшие цены на рынке')

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

async def on_startup(dispather):
    await set_commands(dispather.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)