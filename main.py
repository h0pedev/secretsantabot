import telegram
# import urllib3
# from telegram.ext import Updater

TOKEN = '609040137:AAHxqQK_4qIB4sLQgLJoGjT309R5Nc6Op4s'
# REQUEST_KWARGS = {
#     'proxy_url': 'http://62.80.178.24:34766'
#     # Optional, if you need authentication:
#     # 'urllib3_proxy_kwargs': {
#     #     'username': '3559738',
#     #     'password': '3559738',
#     # }
# }

bot = telegram.Bot(TOKEN)

print(bot.get_me())
