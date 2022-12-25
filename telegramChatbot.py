import telegram.ext

with open("config.txt") as f:
    token = f.read().strip()


bot = telegram.Bot(token=token)


updater = telegram.ext.Updater(bot=bot, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):  update.message.reply_text('hello this bot was created by Atsi25')


def help(update, context): update.message.reply_text('''
    /help 
    /contact -> You can call Atsi25 
    /Lichess  -> You can follow Atsi25 at Lichess
    /Chess  -> You can follow Chess at Chess
    /gitHub -> You can follow Atsi25 projects.
    

''')


def contact(update, context):  update.message.reply_text('Atsi25 contact: 0542397720')


def Lichess(update, context):  update.message.reply_text(
    'https://Lichess.org/atsi25')


def Chess(update, context): update.message.reply_text(
    'https://Chess.com/atsi25')


def github(update, context): update.message.reply_text(
    'https://github.com/emmanuelatikese')



dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('Lichess', Lichess))
dispatcher.add_handler(telegram.ext.CommandHandler('Chess', Chess))
dispatcher.add_handler(telegram.ext.CommandHandler('github', github))

updater.start_polling()
updater.idle()
updater.stop()
