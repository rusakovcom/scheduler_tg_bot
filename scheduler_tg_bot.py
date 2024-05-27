import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

# Specify 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID'
bot_token = 'token'
chat_id = 'chatid'

bot = telegram.Bot(token=bot_token)

def send_message():
    bot.send_message(chat_id=chat_id, text="test message")

# Set up the scheduler
scheduler = BlockingScheduler(timezone=pytz.utc)

# Schedule the job to run

scheduler.add_job(send_message, 'cron', hour=22, minute=0) # Schedule the job to run every day at 22:00 MSK

# Start the scheduler
if __name__ == "__main__":
    scheduler.start()

