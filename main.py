from telebot import TeleBot, types
import schedule
from threading import Thread
import time
import config
import keyboards as kb
from service import GameService
from handlers import invite_code, game
from database import create_all_table

import models 


create_all_table()

bot = TeleBot(config.TOKEN)

def schedule_pending():
    schedule.every(10).seconds.do(GameService.update_coins)
    while True:
        schedule.run_pending()
        time.sleep(1)

    
@bot.message_handler(commands=["start"])
def handle_start(message: types.Message):
    reg = GameService().check_user_or_register(message.from_user)
    if not reg:
        bot.send_message(
            message.chat.id,
            "С возращением",
            reply_markup=kb.start_game_kb
        )
        return
    bot.send_message(
        message.chat.id,
        (
            "Привет, фармер!"
            "тут нужно задротить ради нечего, удачи!"
        ),
        reply_markup=kb.start_game_kb
    )


invite_code.CallbackHandler(bot) 

game.CallbackHandler(bot)


Thread(target=schedule_pending).start()

print("Бот запущен")
bot.infinity_polling()
