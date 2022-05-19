#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.


# Use the application default credentials
#print time.strftime("%a %b %d %H:%M:%S %Y", parsed)



import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



cred = credentials.Certificate("./credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client(app)

API_TOKEN = '5236938866:AAHjpizVSK-YrigfSsU5uq1rHV0pAkaQDNI'
bot = telebot.TeleBot(API_TOKEN)

doc_ref = db.collection(u"sensors").document(u"0")
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
        bot.reply_to(message, 'Comandi:\nElenco comandi: /help\nTemperatura classe: /temperatura\n'
                              'Umidità classe: /umidita\n'
                              'Luminosità classe: /luminosita\n'
                              'Tutti i valori: /all\n'
                              'Informazioni bot: /info\n')

        #dati presi dal sito
    if message.text == '/all':
        bot.reply_to(message, "Ultima temperatura registrata: " + str(doc_ref.get().to_dict()["temp"]) + "°C\n"+
                      "Ultima umidità registrata: " + str(doc_ref.get().to_dict()["hum"]) + "%\n"+
                      "Ultima luminosità registrata: " + str(doc_ref.get().to_dict()["light"]) + "%")

    if message.text == '/temperatura':
        bot.reply_to(message,"Ultima temperatura registrata: "+str(doc_ref.get().to_dict()["temp"])+"°C")
    if message.text == '/umidita':
        bot.reply_to(message,"Ultima umidità registrata: "+str(doc_ref.get().to_dict()["hum"])+"%")
    if message.text == '/luminosita':
        bot.reply_to(message,"Ultima luminosità registrata: "+str(doc_ref.get().to_dict()["light"])+"%")








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
        bot.reply_to(message, 'Questo bot è in grado di prendere le temperatura,umidità,luminosità dal sito '
                              'scudo-project.web.app e mandartele qui.')



    if message.text == 'ciaccio è bello':
        bot.reply_to(message, 'si lo so')
    if message.text == 'Archimede è la miglior scuola':
        bot.reply_to(message , 'non te la consiglio MARANZA')
    if message.text == 'Autori':
        bot.reply_to(message, "Classe 4ft-i")
    if message.text == 'sito':
        bot.reply_to(message, 'scudo-project.web.app')
    if message.text == 'Sito':
        bot.reply_to(message, 'scudo-project.web.app')










bot.infinity_
