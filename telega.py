from telegram.ext import Updater
from telegram.ext import CommandHandler


request_kwargs = {
    'proxy_url': 'socks5://89.223.92.30:9011',
    'urllib3_proxy_kwargs':{
        'username': 'kek',
        'password': 'kek',
    }
}


updater = Updater(token='792596132:AAEwLQ-vPFryBLsLnC7KAFzrI1rvIBMlWZk', use_context=True, request_kwargs=request_kwargs)
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="GOLD ON MY WIRST FUCK THE POLICE")



start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
updater.start_polling()
