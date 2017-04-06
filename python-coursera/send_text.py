from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC6c0ea0030adb7f4b08f58be982e8b27b"
# Your Auth Token from twilio.com/console
auth_token  = "1b40a202bafd492d07ba7cb32a9d8eb5"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+19842428463", 
    from_="+16123602449",
    body="SND?")

print(message.sid)