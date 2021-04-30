import schedule
import time
from app import send_sms

def job() :
    send_sms()

schedule.every().day.at("04:30").do(job)
schedule.every().day.at("06:30").do(job)
schedule.every().day.at("09:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)