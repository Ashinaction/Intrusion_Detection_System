from twilio.rest import Client

account_sid = 'AC6e8acd79309e98acc6029736c470a84e'
auth_token = 'dbf81462ccda496a940c638e890445e5'
client = Client(account_sid, auth_token)

def sendSms():
  message = client.messages.create(
     from_='+18577545477',
     body='ALERT',
     to='+918318140410'
  )
  return message
 
message=sendSms()
print(message.sid)
