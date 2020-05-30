import dialogflow_v2beta1 as dialogflow
import datetime
from google.protobuf.json_format import MessageToJson
import json
import csv
import time
import os
import csv

credentials_path = 'gracie.json'
project_id='gracie-ucroqs'

class Session_Client:

    def __init__(self,credentials_path=credentials_path, project_id=project_id):
        self.project_id = project_id
        self.session_client = dialogflow.SessionsClient.from_service_account_json(credentials_path)
        self.session_ = self.session_client.session_path(self.project_id,'1001')
    
    def detectIntent(self,text):
        text_input = dialogflow.types.TextInput(text=text, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        return self.session_client.detect_intent(session=self.session_, query_input=query_input)

    def dialogflow(self, question):

        resp = self.detectIntent(question)
        json_response = MessageToJson(resp)
        r = json.loads(json_response)

        print(r)
        responseId = r['responseId']
        queryResult = r['queryResult']
        queryText = queryResult['queryText']
        intent = queryResult['intent']
        action = queryResult['action']
        parameters = queryResult['parameters']
        order = ""

        f = open('price.json')
        price = json.load(f)

        if queryResult['action'] == 'order_veg':
            veg = parameters['vegetables']
            quan = parameters['number']

            if len(veg) != len(quan):
                for x in range(len(veg) - len(quan)):
                    parameters['number'].append(1.0)

            for i in range(len(veg)):
                veggie = veg[i]
                
        
            return queryText, order
            
        else:
            return queryText, "I'm sorry I don't think I understand"
