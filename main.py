import requests
from random import randint
from bs4 import BeautifulSoup as b
import telebot

#подключение бота
bot = telebot.TeleBot('5376411642:AAEl1NEVzuih6MxXEKfbYocc-Eey_jKw2Ec', parse_mode=None)
id = '1347043446'
#приветствие
@bot.message_handler(commands=['start', 'help', 'anecdot'])
def send_welcome(message):
    bot.reply_to(message, 'Прив, хочешь вылечиться от дисперсии? Тогда каждый раз, когда ты не будешь здоров, пиши: "Склеивай". А когда ты поймешь, что тяжелая болезнь тебя покинула, напиши "Спасибо, я склеился"')


@bot.message_handler(func=lambda mess: True)
def send_anec(mess):
    r2 = requests.get("https://www.anekdot.ru/last/good/").text
    soup = b(r2, "html.parser")
    anekdots = soup.find_all("div", class_="text")
    #print(anekdots)
    clear_anek = [c.text for c in anekdots]
    #print(clear_anek)
    if mess.text == 'Склеивай':
        bot.reply_to(mess, clear_anek[randint(1, len(clear_anek) - 1)])
    elif mess.text == 'Спасибо, я склеился':
        bot.reply_to(mess, 'Были рады с вами поработать, больше не расклеивайтесь!')
    else:
        bot.reply_to(mess, 'Писать научись, идиотик')

r2 = requests.get("https://api.telegram.org/bot5376411642:AAEl1NEVzuih6MxXEKfbYocc-Eey_jKw2Ec/getUpdates").text
r2 = requests.post('https://api.telegram.org/bot5376411642:AAEl1NEVzuih6MxXEKfbYocc-Eey_jKw2Ec/sendMessage',data={'chat_id':id,'text': 'Прив, хочешь вылечиться от дисперсии? Тогда каждый раз, когда ты не будешь здоров, пиши: "Склеивай". А когда ты поймешь, что тяжелая болезнь тебя покинула, напиши "Спасибо, я склеился"'}).text

print(r2)
bot.infinity_polling()
