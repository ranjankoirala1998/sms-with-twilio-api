from twilio.rest import Client
from scrapper import get_body

account_sid = "AC3baaf8b11c7ba6d6064fa41f2d2346f3"
auth_token = "c51620a26d68b078623ddb45f9ff7895"

my_phone_num = "+9779862074364"

def send_sms():
    client = Client(account_sid, auth_token)

    sms = client.messages.create(

        from_= "+17725772292",
        body = get_body(),
        to = my_phone_num

    )

    print("Executed Successfully!!")




