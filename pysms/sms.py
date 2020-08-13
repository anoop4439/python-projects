from twilio.rest import Client 
 
account_sid = '***************' # need to enter the twilio account sid
auth_token = '*************' # need to enter the twilio auth token
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+1xxxxxxxxxxxx', # from number should be the twilio number we have
                              body='First python message to phone',        
                              to='+91xxxxxxxxxxx' # to number is the receipient number
                          ) 
 
print(message.sid)