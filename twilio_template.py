# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Message Text Goes here..",
    from_="ENTER TWILIO PROVIDED NUMBER",
    to="ENTER YOUR REGISTERED TWILIO NUMBER",
)

print("Message Status: "+message.status)