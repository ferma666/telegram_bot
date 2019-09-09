from telegram.ext import Updater
from telegram.ext import CommandHandler
import random


request_kwargs = {
    'proxy_url': 'socks5://84.53.239.112:8888',
    'urllib3_proxy_kwargs':{
        'username': 'kek',
        'password': 'kek',
    }
}


updater = Updater(token='792596132:AAEwLQ-vPFryBLsLnC7KAFzrI1rvIBMlWZk', use_context=True, request_kwargs=request_kwargs)
dispatcher = updater.dispatcher


def start(update, context):
    print(update)
    context.bot.send_message(chat_id=update.message.chat_id, text="DAUN")


def pidor(update, context):
    print(update)
    ty_pidor = bool(random.getrandbits(1))
    if ty_pidor:
        message = "Ты пидор :CC"

    else:
        message = "Тебе на этот раз повезло"

    context.bot.send_message(chat_id=update.message.chat_id, text=message)


start_handler = CommandHandler('start', start)
pidor_handler = CommandHandler('pidor', pidor)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(pidor_handler)
updater.start_polling()
