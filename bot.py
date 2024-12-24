import telebot
import random 
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7420968680:AAEypibz6LynVhgtUpKHv26H49Nl1dOV0dM")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/help \n/start \n/hello \n/bye \n/help \n/random \n/eco")

@bot.message_handler(commands=['random'])
def send_random(message):
    numb = random.randint(1,50)
    bot.reply_to(message, f"тебе выпало случайное число {numb}")


@bot.message_handler(commands=['eco'])
def send_eco(message):
    bot.reply_to(message, "Првет! Я буду стараться помогать людям навести порядок на планете. Чтобы начать тебе надо сделать три  вещи: сортировать мусор, следить за тем какие продукты ты покупаешь и больше уделять внимания животному миру")

 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
