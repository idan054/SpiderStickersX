from twilio.rest import Client

account_sid = 'AC7821176e32b0282cd658d55bc617204f'
auth_token = '73f5828b381844b9ef134f91a6c0e881'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='הודעה זו נשלחה דרך רובוט הפייתון של Twil3io',
    to='whatsapp:+972522509900'
    # to='whatsapp:+972584770076'
)

print(message.error_code)
print(message.status)