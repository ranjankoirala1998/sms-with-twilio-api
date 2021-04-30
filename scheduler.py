import schedule
import time
from app import send_sms

def job() :
    send_sms()

schedule.every(60).seconds.do(job)

# schedule.every().day.at("10:15").do(job)
# schedule.every().day.at("12:15").do(job)
# schedule.every().day.at("15:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)