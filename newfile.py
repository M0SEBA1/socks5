import requests
import telebot
token = "5240936024:AAFNS6pv3gCFVmCxxUjiWJdgC0GZJRpWFx8" #حط توكن شنو منتضر 
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
 #اخخ اشوفك كاعد تنسخ
 bot.send_message(message.chat.id, f"""
• مرحبا نورت بوت بروكسي جميع الانواع 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
ـ [socks4] ـ [socks5] ـ [http] ـ [https] ـ
 ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
• عزيزي المستخدم اكتب نوع الذي تريد ...
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
 المبرمج : @M0SEBA """)
 @bot.message_handler(func=lambda followinG:True )
 def re(message):
  zood =(message.text)
  pp = zood
  url = requests.get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=100000000000000&country=all&ssl=all&anonymity=all').text
  prox = url.split('\r\n')
  for ee in prox:
    bot.send_message(message.chat.id,ee)
bot.polling(True)