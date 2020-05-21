import telebot
from telebot import types

bot = telebot.TeleBot("1136374001:AAHsgwhJXmxOS7KUyqx_HOu-r2YBk7mTia")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I'm Mykhailo Tkachenko and this is my CV bot :)")


@bot.message_handler(commands=['exp'])
def send_about(message):
    bot.send_message(message.chat.id, """
I start my code expierence in 15 years old in Python, than i moved to C++, and than in Kotlin.
On Kotlin I write about one year. All my expiernce this is my projects and course, for learning Kotlin.
I took a course in Udemy. Than start to code an app for check a Covid-19 status and track this virus in world, i have this project on GitHub.
This is a simple app with quiz for check status and than you have instructions what you must do if you are ill or not, also in this app you can see a Covid-19 in the world.
After this app i start code another app. This app a messanger with encrypting messenges in real time.
You can encrypt messeges cezars cipher with cipher key. This app use firebase for sign-up with email and photo.
Also firebase i use for save messeges and all data about users. This app you can download from Google Play and i have repository on GitHub.

P.S
For links on GitHub and Play Market you can write /projects """)


@bot.message_handler(commands=['projects'])
def send_projects(message):
    keyboard_git = types.InlineKeyboardMarkup(row_width=30)
    keyboard_play = types.InlineKeyboardMarkup(row_width=30)
    url_button_covid_git = types.InlineKeyboardButton(text="Covid-19", url="https://github.com/m-tkachenko/Covid_19")
    url_button_cipher_git = types.InlineKeyboardButton(text="CipherMe", url="https://github.com/m-tkachenko/CipherMe")
    url_button_cipher_play = types.InlineKeyboardButton(text="CipherMe",
                                                        url="https://play.google.com/store/apps/details?id=com.saloYD.ciphermessage")

    keyboard_git.add(url_button_covid_git)
    keyboard_git.add(url_button_cipher_git)
    bot.send_message(message.chat.id, "GitHub links", reply_markup=keyboard_git)

    keyboard_play.add(url_button_cipher_play)
    bot.send_message(message.chat.id, "PlayMarket links", reply_markup=keyboard_play)


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, """
Name: Mykhailo Tkachenko
Age: 17
Motherland: Ukraine
Live: Poland
Languages: Ukranian, English, Polish, Russian
University: Collegium Da Vinci, start in 2019 

Linkedin: https://www.linkedin.com/in/mykhailo-tkachenko/
Upwork: https://www.upwork.com/freelancers/~01ccc97fa5f275f005?s=996364627857502209
GitHub: https://github.com/m-tkachenko
Telegram: https://t.me/gibygreen""")

bot.polling()
