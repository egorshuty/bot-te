#input your telegram token in config.py
import sys
import config
import telebot
from telebot import types
import time
import xlsxwriter
import random
bot = telebot.TeleBot(config.token)
markup = types.ReplyKeyboardMarkup()
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.


num = {}

@bot.message_handler(commands=['start']) #for /startasfasfaseasfasf asf asf s f 
def handle_start_help(message):
    bot.send_message(message.chat.id,"Здравствуйте,я бот-диджей")
    bot.send_message(message.chat.id,"Сбрасывайте мне ваши топовые треки под которые вы будете флексить на дискотеке,только названия треков!О всем остальном мы позаботимся сами.")
    bot.send_message(message.chat.id,'Сбрасывайте отдельным сообщение)')
    print(message.text,message.chat.id)
   


@bot.message_handler(content_types=['text']) 
def music(message):
    bot.send_message('717287471',message.text)
    replie = random.randrange(1, 8)
    if replie == 1:
        bot.send_message(message.chat.id, 'Отлично!Чем больше треков тем лучше!')
    if replie == 2:
        bot.send_message(message.chat.id, 'Пушка!Нам важен каждый ваш трек')
    if replie == 3:
        bot.send_message(message.chat.id, 'Воу!Больше годноты!')
    if replie == 4:
        bot.send_message(message.chat.id, 'Больше!Больше треков!')
    if replie == 5:
        bot.send_message(message.chat.id, 'Хорошо!Найдешь еще что-то кидай мне')
    if replie == 6:
        bot.send_message(message.chat.id, 'Ого,а у тебя хороший вкус!')
    if replie == 7:
        bot.send_message(message.chat.id, 'Спасибо!Встретимся на дискотеке!')
    if replie == 8:
        bot.send_message(message.chat.id, 'Greate,see на дискотеке!')
def on_exit_by_ctrl_c(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        quit()
    else:
        _old_excepthook(exctype, value, traceback)
 
sys.excepthook = on_exit_by_ctrl_c        
 

   

workbook.close()

    
if __name__ == '__main__':
     bot.polling(none_stop=True)

if message.text == "exit":
    exit()