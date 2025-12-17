import nltk
'''nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')'''

#nltk.data.find('tokentizers/punkt')
#nltk.data.find('corpora/stopwords')
#import random
#from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
'''stop_words=set(stopwords.words('english'))
text="hello nova,how are you today?"
tokens=[word.lower() for word in word_tokenize(text) if word.lower() not in stop_words]
print(tokens)'''
def greet():
    print("chatbot:Hello")
    print("chatbot:Im your friendly chatbot")
    print("tou can ask for time,jokes,quotes")
    print("chatbot:Type'bye' to exit.\n")
stop_words=set(stopwords.words('english'))
response={
    "hello":"hello! how can I help you?",
    "hi":"hi there",
    "how are you":"Im doing great! thanks for asking",
    "your name":"My name is Nova",
    "bye":"see u soon Have a nice day"
}
def get_response(user_input):
    for k in response:
        if k in user_input:
            return response[k]
    return "sorry i couldnt understand"
    
def chatbot():
    greet()
    while True:
        user_input=input("you:").lower()
        response=get_response(user_input)
        print("chatbot",response)
        if "bye" in user_input:
            break
chatbot()