# A slightly modernized version of the AfricasTalkingGateway class
# supplied by africastalking.com.

import simplejson
import requests

class AfricasTalkingGateway:
    def __init__(self, username_, apiKey_):
        self.username=username_
        self.apiKey=apiKey_

        self.URLString="https://api.africastalking.com/version1/messaging"

    def sendMessage(self, to_, message_, from_="", bulkSMSMode_=1):
        
        values={'username':self.username,
                'to':to_,
                'message':message_}

        if len(from_) > 0:
            values["from"] = from_
            values["bulkSMSMode"]=bulkSMSMode_

        headers={'Accept':'application/json',
                 'apiKey':self.apiKey}

        data=simplejson.dumps(values)
        response = requests.post(self.URLString, data, headers=headers)

        recipients=response.content['SMSMessageData']['Recipients']
        return recipients
        
    def fetchMessages(self, lastReceivedId_):
        url="%s?username=%s&lastReceivedId=%s" % (self.URLString, self.username, lastReceivedId_)

        headers={'accept':'application/json',
                 'apikey':self.apiKey}

        response=requests.get(url)
        messages=response.json()['SMSMessagesData']['Messages']

        return messages
