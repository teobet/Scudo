#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '5236938866:AAHjpizVSK-YrigfSsU5uq1rHV0pAkaQDNI'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao , benvenuto nel bot dell'Archimede.
Per visualizzare l'elenco dei comandi digita:\n/help\n\
""")



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == '/help':
        bot.reply_to(message, 'Comandi:\nElenco comandi: /help\nTemperatura classe: /tempClasse\n'
                              'Umidità classe: /umiditaClasse\n'
                              'Informazioni bot: /info')

    if message.text == 'Ciao':
        bot.reply_to(message, 'Ciao  come va ?')
    elif message.text == 'Bene':
        bot.reply_to(message, 'Mi fa piacere')
    elif message.text == 'bene':
        bot.reply_to(message, 'Mi fa piacere')
    elif message.text == 'Bene tu?':
        bot.reply_to(message, 'Bene grazie.')
    elif message.text == 'bene tu?':
        bot.reply_to(message, 'Bene grazie.')
    elif message.text == 'bene tu':
        bot.reply_to(message, 'Bene grazie.')
    elif message.text=='Bene tu':
        bot.reply_to(message,'Bene grazie.')

    if message.text == 'ciao':
        bot.reply_to(message, 'Ciao come va ?')

    if message.text == '/info':
        bot.reply_to(message, 'Questo bot è in grado di prendere le temperature dal sito '
                              'scudo-project.web.app e mandartele qui.')
    if message.text == '/Info':
        bot.reply_to(message, 'Questo bot è in grado di prendere le temperature dal sito '
                              'scudo-project.web.app e mandartele qui.')








bot.infinity_polling()