import telegram
import os
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# specify token and chat_id from .env
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telegram.Bot(token=bot_token)


# define function to send messages
def send_message(text):
    bot.send_message(chat_id=chat_id, text=text)


# Set up the scheduler
scheduler = BlockingScheduler(timezone=pytz.timezone('Europe/Moscow'))

# Schedule the jobs to run at specific times

message1 = 'test message every day at 21:50 msk'
scheduler.add_job(send_message, 'cron', hour=21, minute=50, args=[message1])

message2 = 'test message every day at 20:00 msk'
scheduler.add_job(send_message, 'cron', hour=20, minute=0, args=[message2])

message3 = 'test message every day at 20:25 msk'
scheduler.add_job(send_message, 'cron', hour=20, minute=25, args=[message3])


# Start the scheduler
if __name__ == "__main__":
    scheduler.start()
