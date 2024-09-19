import telebot
from telebot import types
import threading
import time
bot = telebot.TeleBot = input("Token Bot 1 :")
bot2 = telebot.TeleBot = input("Token Bot 2 :")

chat_id = input("Numeric ID of the group :")


sending = False

ready = input("Write “attack” to start bot1:")
textbot1 = input("text1:")
text2bot1 = input("text2:")
if ready.lower() == "attack":
    sending = True

    def send_message():
        global sending  # به متغیر sending در سطح جهانی دسترسی پیدا میکنیم
        while sending:
            try:
                bot.send_message(chat_id, textbot1)
                bot.send_message(chat_id, text2bot1)

                time.sleep(0)  # زمان خواب بین پیام‌ها

            except Exception as e:
                print(f"Error: {e}")  # ردیابی خطا

    thread = threading.Thread(target=send_message)
    thread.start()
else:
    print("The attack bot1 was cancelled!")
ready = input("Write “attack” to start bot2:")
textbot2 = input("text1:")
text2bot2 = input("text2:")
if ready.lower() == "attack":
    sending = True

    def send_message():
        global sending  # به متغیر sending در سطح جهانی دسترسی پیدا میکنیم
        while sending:
            try:
                bot2.send_message(chat_id, textbot2)
                bot2.send_message(chat_id, text2bot2)
                time.sleep(0)  # زمان خواب بین پیام‌ها

            except Exception as e:
                print(f"Error: {e}")  # ردیابی خطا

    thread = threading.Thread(target=send_message)
    thread.start()
else:
    print("The attack bot1 was cancelled!")
# برای اجرای ربات
if name == "__main__":  # اگر name برابر "main" باشد این قسمت اجرا می‌شود
    bot.polling()