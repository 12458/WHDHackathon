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
            
            leafy = ['wheat grass', '']

            ## Iterating through all the vegetables in the parameters
            for i in range(len(veg)):
                veggie = veg[i].lower()
                ## Iterating through the vegetable categories in price.json
                for cate in price.keys():
                    ## If the vegetable type is part of the vegetable categories name
                    if veggie in cate:
                        variety1 = price[cate]
                        selection = []
                        for product in variety1.keys():
                            if veggie.capitalize() in product:
                                selection.append(product)

                        chosen_veg = input(f"Please provide the full name of the product you'd like to purchase: {selection}\n")

                        while chosen_veg not in selection:
                            chosen_veg = input(f"Please provide the full name of the product you'd like to purchase: {selection}\n")
                        
                        with open("order_list.csv", "a") as file:
                            f = csv.writer(file)
                            list1 = [f"{chosen_veg}", f"{quan[i]}", f"{variety1[chosen_veg]}"]
                            f.writerow(list1)
            
            with open("order_list.csv", "r") as file2:
                total_cost = 0
                for row in file2:
                    row = row.split(",")
                    total_cost += float(row[2])
                    order += "Product Name: " + row[0] + ", Quantity: " + row[1].strip(".0") + ", Unit Price: $" + row[2]
            
            order += "Total Cost: $" + str(total_cost)

            with open("order_list.csv", "w") as file3:
                pass
        
            return queryText, order
            
        else:
            return queryText, "I'm sorry I don't think I understand"
