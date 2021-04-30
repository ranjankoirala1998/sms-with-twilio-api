from twilio.rest import Client
from scrapper import get_body
from os import environ

account_sid = environ['ACCOUNT_SID']
auth_token =  environ['AUTH_TOKEN'] 


phone_num = '+9779862074364'

def send_sms():
    client = Client(account_sid, auth_token)

    sms = client.messages.create(

        from_= '+17725772292',
        body = get_body(),
        to = phone_num

    )



