from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC1eaf61ebe377cc0ce330980ac4b3c1a2'
auth_token = '57d76d3d15a4ecf5b90a8f00e49eefe8'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+918727848306',                        				from_='+18125754021'
                    )

print(call.sid)
