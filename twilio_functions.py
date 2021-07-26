from twilio.rest import Client
from secrets import sid, token, twilio_number


client = Client(sid, token)


def twilio_call(number_to_call):
    
    client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                        to=number_to_call,
                        from_=twilio_number)


def twilio_text(text_message, number_to_text):

    client.messages.create(body=text_message,
                            from_=twilio_number,
                            to=number_to_text)


if __name__ == '__main__':
    
    pass
