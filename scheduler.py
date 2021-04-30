import schedule
import time
from app import send_sms

def job() :
    send_sms()

schedule.every().day.at("4:30").do(job)
schedule.every().day.at("6:30").do(job)
schedule.every().day.at("9:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)