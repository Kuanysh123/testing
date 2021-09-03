import telebot
#from telebot import types
import config
bot = telebot.TeleBot(config.TOKEN)


name = ''
cv = ''
fio = ''
num = 0

@bot.message_handler(commands=['start'])
def start_er(message):
    bot.send_message(message.from_user.id, 'Здраствуйте! Выберете Бизнес Центр!')
    bot.register_next_step_handler(message, reg_bc)

def reg_bc(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая квадратура вас интересует?')
    bot.register_next_step_handler(message, reg_cv)

def reg_cv(message):
    global cv
    cv = message.text
    bot.send_message(message.from_user.id, 'Ваше ФИО?')
    bot.register_next_step_handler(message, reg_fio)

def reg_fio(message):
    global fio
    fio = message.text
    bot.send_message(message.from_user.id, 'Ваш номер телефона?')
    bot.register_next_step_handler(message, reg_num)

def reg_num(message):
    global num
    if num == 0:
        try:
            num = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вы что-то не то написали!\nМне нужен ваш номер телефона!')
    question = 'Перепроверьте вашу информацию!\n-------------------------------\n' + 'Ваше имя: ' + fio + '\n' + 'Бизнес Центр: ' + name + '\n' + 'Интересующая вас квадратура: ' + cv + '\n' + 'Ваш номер телефона: ' + str(num) + '\n' + '--------------------------------' + '\n' + 'Все ли правильно?'
    bot.send_message(message.from_user.id , question )


bot.polling(none_stop=True, interval=0)