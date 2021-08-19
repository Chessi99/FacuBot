import telebot
from decouple import config
from helpers.helpers import get_parameters
from service.Service import Service

API_TOKEN_BOT = config('TOKEN_BOT')
bot = telebot.TeleBot(API_TOKEN_BOT, parse_mode=None)

service = Service()

# /agregar_materia NOMBRE_MATERIA, NUMERO_SEMESTRE
@bot.message_handler(commands=['agregar_materia', 'help'])
def add_subject(message):
    parameters = get_parameters(message.text)
    print(parameters)
    if len(parameters) != 2:
        bot.reply_to(message,"La cantidad de parametros son 2 con la forma NombreMateria, NumeroSemestre")
        return
    
    subject = parameters[0]
    semester_number = parameters[1]
    ok = service.add_subject(subject, int(semester_number))
    if ok:
        bot.reply_to(message, f"Agregada la materia {subject}")
    else:
        bot.reply_to(message, f"La {subject} ya fue agregada previamente")



if __name__ == '__main__':
    bot.polling()

