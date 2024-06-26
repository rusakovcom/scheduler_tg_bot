import logging
import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

# load .env file vars
load_dotenv()

# token
bot_token = os.getenv("BOT_TOKEN")

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    print(f"Your chat ID is: {chat_id}")
    update.message.reply_text(f"Your chat ID is: {chat_id}")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Add a handler for text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_chat_id))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
