# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import dialogflow_v2beta1
from google.api_core.exceptions import InvalidArgument
import os
#print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
DIALOGFLOW_PROJECT_ID = 'sakshi-qrsost'
DIALOGFLOW_LANGUAGE_CODE = 'en-IN'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./sakshi-qrsost-f5c6078322da.json"
#GOOGLE_APPLICATION_CREDENTIALS = './sakshi-qrsost-f5c6078322da.json'
print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
SESSION_ID = 'divyang'

session_client = dialogflow_v2beta1.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
while 1==1:

	text_to_be_analyzed = input("Query Text: ")
	text_input = dialogflow_v2beta1.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
	query_input = dialogflow_v2beta1.types.QueryInput(text=text_input)
	try:
	    response = session_client.detect_intent(session=session, query_input=query_input)
	except InvalidArgument:
	    raise
	if response.query_result.intent == 'sakshi.emergency':
		response.query_result.fulfillment_text = 'hehehe'
	#print("Query text:", response.query_result.query_text)
	#print("Detected intent:", response.query_result.intent.display_name)
	print("Detected intent confidence:", response.query_result.intent_detection_confidence)
	print("Fulfillment text:", response.query_result.fulfillment_text)
