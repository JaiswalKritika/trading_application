# import telebot
# from core.settings import TELEGRAM_BOT_TOKEN



# bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)
# @bot.message_handler(commands=["help","hello"])
# def send_help_message(msg):
#     bot.reply_to(msg,"Hello! This is a test bot")


# to restrict it to text
# @bot.message_handler(content_types=["photo","sticker"])
# def send_content_message(msg):
#     bot.reply_to(msg,"this is not a text message")


# to restrict for a certain user
# @bot.message_handler(content_types=["photo","sticker"])
# @bot.message_handler(func=lambda msg: msg.from_user.usrname == "username")
# def send_content_message(msg):
#     bot.reply_to(msg,"this is not a text message")

# @bot.edited_message_handler(commands=["noice"])
# def send_multiple_message(msg):
#     bot.send_message(chat_id=msg.chat.id,text="WOW! done")

# bot.polling()