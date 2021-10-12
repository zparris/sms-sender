  
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'ACf240a9fc2320364583db8c1025651d50'
auth_token = '02ff12e8202860aaaf96ced77498cee8'
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+447596195922",
    from_="+447575753273",
    body="Sorry Zahir cant take part in PE today :P")

print(message.sid)
