from telegram import Bot

bot = Bot(token="7872406811:AAH5Hu8NRmI5TMGKtIm4AXzDSIPDo0A_HIU")
updates = bot.get_updates()
for u in updates:
    print(u.message.chat.chat_id, "-", u.message.chat.title)

