import spacy
import en_core_web_sm
from nltk import sent_tokenize
from flask import jsonify

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

class pos(my_dictionary):
    def __init__(self):
        super().__init__()
        self.nlp = en_core_web_sm.load()
        print("NLP model Loaded")

    def result(self,text):
        sentences = sent_tokenize(text)
        dict_obj = my_dictionary() 
        for text in sentences:
            doc = self.nlp(text)
            result = []
            for token in doc:
                if(token.pos_=='NOUN'):
                    result.append(token.text)
            dict_obj.add(text,result)
        return dict_obj

# Initialize the class object 
pos_obj = pos()
