import telebot

# ضع هنا توكن البوت الخاص بك
BOT_TOKEN = "7628396387:AAHWYlcoXPlonzhCmimp0g0ybJEGT8zKUd8"

# إنشاء البوت
bot = telebot.TeleBot(BOT_TOKEN)

# الاستماع للرسائل
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"لقد أرسلت: {message.text}")

# تشغيل البوت
bot.polling()
