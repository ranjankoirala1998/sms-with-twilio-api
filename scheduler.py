import schedule
import time
from app import send_sms

def job() :
    print("I am running...")

schedule.every(10).seconds.do(job)

# schedule.every().day.at("10:15").do(job)
# schedule.every().day.at("12:15").do(job)
# schedule.every().day.at("15:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)