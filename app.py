from twilio.rest import Client
from scrapper import get_body

account_sid = <Account SID>             # Use the actual account sid
auth_token = <Authentication Token>     # Use the actual authentication token

phone_num = <recipient_number>          # Use the actual recipient number

def send_sms():
    client = Client(account_sid, auth_token)

    sms = client.messages.create(

        from_= <sender_number>,         # Use the actual sender number
        body = get_body(),
        to = phone_num

    )

    print("Executed Successfully!!")

send_sms()




