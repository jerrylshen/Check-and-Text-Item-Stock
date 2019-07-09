#Go to Twilio and get an account. Get these info in dashboard
account_sid = XXXXXXXXXXXXXXXXXXXXXXXXX
auth_token = XXXXXXXXXXXXXXXXXXXX
client = Client(account_sid, auth_token)

#if multiple phone numbers, iterate through them. If single, no need for this list
phone_numbers = ["+XXXXXXXXXXXXXX", "+XXXXXXXXXXXX"]

#a simple alert text message w/ link
def send_alert():
    for number in phone_numbers:
        message = client.messages \
                    .create(
                         body="\t\t\n"
                              "https://www.holotaco.com/products/holo-taco-launch-collection \n"
                              "Not sold out"
                              ,
                         #get a Twilio number
                         from_='+XXXXXXXXXXXXXXX',
                         to=number
                         )

#print(message.sid)
