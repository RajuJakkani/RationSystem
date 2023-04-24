from twilio.rest import Client

TWILIO_NUMBER = "+15074178219"
TO_NUMBER = "+918263994073"

account_sid = "AC5e8d5116cffac2b2c9e452abd99691c0"
auth_token = "24bbe1b20ae3fbd8b3cd80ce1dc9ce5d"

client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Hello there from Twilio SMS API',
         from_ =  TWILIO_NUMBER,
         to = TO_NUMBER
)

print(message.body)