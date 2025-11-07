
from basic import *
import telebot
import random
from flask import Flask
import threading

# a servve to alive bot
app = Flask(__name__)

@app.route("/")
def homepage():
    return  'Welcome to AntiBot!'



#creat my frist bot
antiBot = telebot.TeleBot('8596596102:AAGQ0y4TlOjUWPmUdaKVYv5hnCy3XBoUonk')
#strat bot code
@antiBot.message_handler(commands=['start'])
def send_welcome(mas):
    antiBot.reply_to(mas, "سلام بیاید ثمری رو اذیت کنیم")


@antiBot.message_handler(commands=['help'])
def send_help(mas):
    if mas.chat.type == "private":
         antiBot.reply_to(mas, "این برنامه هیچ کاری جز تخریب ثمری نیکنه")
    elif mas.chat.type == "group" or mas.chat.type == "supergroup":
        antiBot.reply_to(mas, "این ربات درصورت دریافت پیام از سمت ثمری جواب میده و در کل خیلی مودبه. \n درصورتی که فحشی پشتیبانی نشده لطفا به آیدی سازنده اطلاع دهید.\n اگر جواب پیشنهادی دارید بگید \n نظرات درباره بهبود تخریپ ثمری رو ارسال کنید \n باتشکر")

@antiBot.message_handler(func=lambda m: True)
def main(mes):
    # id samar
    samari = int(id["samari"])
    first_bool = bool(id["samari"] != "")
    #start
    _or = bool(mes.chat.type == 'private' or mes.chat.type == 'supergroup')

    if mes.chat.type == 'supergroup' and mes.content_type == 'text':
        if mes.from_user.id == samari:
            if "سلام" in mes.text:
                antiBot.reply_to(mes, random.choice(['خواب بودم بیدارم کردی، شمشیر من کوش؟؟؟؟','چه عجب']))

            elif "آنتی" in mes.text or "آنتی ثمری" in mes.text:
                antiBot.reply_to(mes, "چی زر زر میکنی؟")
            elif "لطیف" in mes.text:
                antiBot.reply_to(mes, "پشت ربات قایم شدی ترسو. مرده شور خودت با ارتش رباتیت. ریدی مرد")
            else:
                for badWord in bad_word:
                    if badWord in mes.text:
                        antiBot.reply_to(mes, diction[badWord])
                        continue

        else:
            if "سلام" in str(mes.text):
                ans=   ['سلام عشقم', 'چطوری جیگر', 'عشق میکنی ها...']
                antiBot.reply_to(mes, random.choice(ans))


            elif "آنتی" in mes.text or "آنتی ثمری" in mes.text:
                antiBot.reply_to(mes, random.choice([ "دنبال چی هستی؟، اینقدر پیام بده تا جونت دربیاد. گفتم که منتظر ثمری هستم تا پیام بده", 'حیف نیست ثمری رو اذیت نکردی. حواست باشه عمری که پای نوشتن این پیام گذاشتی از دستت رفته...\n پس اگه نمیخوای ثمری رو اذیت کنی پیام الکی نده']))


            elif "ثمری کیست" in mes.text:
                antiBot.reply_to(mes, f"یک {random.choice(bad_word_ans)}به تمام معنا است")
            elif "ثمری" in mes.text:
                antiBot.message_handler(mes, f"کی؟\nهمون{bad_word_ans}میگی؟" )


            elif True :
                for badWord in bad_word:
                    if badWord in mes.text:
                        antiBot.reply_to(mes, random.choice(list_anser))
                        continue

    elif mes.chat.type == 'private' and mes.content_type == 'text':
        antiBot.reply_to(mes, "دنبال چی هستی؟، اینقدر پیام بده تا جونت دربیاد. گفتم که فقط با ثمری کار دارم")
    else:
        list_anser_notText = ['مسخرتون رو در بیارید منم درمیارم ها','لطفا از کارها بیهوده پرهیز کنید و به ثمری فحش بدید']
        antiBot.reply_to(mes, random.choice(list_anser_notText))



#run flask
def run_flask():
    app.run(host='0.0.0.0', port=8080, debug=True)


threading.Thread(target=run_flask).start()


if __name__ == '__main__':
    antiBot.infinity_polling()


