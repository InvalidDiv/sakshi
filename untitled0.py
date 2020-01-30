# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:42:32 2020

@author: divtech
"""

import dialogflow

# Instantiates a client
client = language.LanguageServiceClient()
# The text to analyze
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))