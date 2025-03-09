from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

answers = {
    "hi": "Hi, How can i help you?😄",
    "schedules": "We are open from Monday to Saturday, from 9 am 🌞 to 7 pm 🌝!",
    "prices": "Subscriptions: 🏋️‍♂️\n - 😊Monthly 30€\n - 😏Three-months 80€\n - 😤Yearly 250€",
    "menu": "Here's our menu:\n - 🍕Pizza 8€\n - 🍔Burger 10€\n - 🥗Salad 6€",
}

async def start(update: Update, context: CallbackContext): 
    await update.message.reply_text("Hi, reply to this message with a word between 'schedules', 'prices' or 'menu' to get more info about one of them!")

async def handle_message(update: Update, context: CallbackContext): 
    text = update.message.text.lower()
    answer = answers.get(text, "I didn't understand. Sorry, reply with 'schedules', 'prices' or 'menu' to get more info about one of them!")
    await update.message.reply_text(answer)

def main(): 
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅Bot started!")
    app.run_polling()

if __name__ == "__main__": 
    main()