from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '*******************************'
auth_token = '********************************'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='***********',                        				from_='**********'
                    )

print(call.sid)
