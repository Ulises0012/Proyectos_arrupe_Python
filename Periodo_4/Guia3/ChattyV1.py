from twilio.rest import Client

account_sid = 'AC0bf8fe0081e2db0b17089d8abd27797e'
auth_token = 'eaf4f4f1691673debbad9ddbd6d10d09'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+50361439068'
)

print(message.sid)