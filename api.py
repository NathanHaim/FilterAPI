import gesture_file
import service
from json_return import jsonR
from flask import Flask, request

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class CleanProhibitedWords(Resource):
    #response if the user does not use the api correctly
    def get(self):
        response = jsonR.copy()
        response['Return'] = False
        response['Message'] = "Get does not exist for this request, you want use put maybe"
        return response

    #clean the list of prohibited words
    def put(self):
        if gesture_file.deleteAllWords():
            response = jsonR.copy()
            response['Return'] = True
            response['Message'] = "List cleaned correctly"
            return response
        else:
            response = jsonR.copy()
            response['Return'] = False
            response['Message'] = "A problem was occured occured"
            return response




class AddProhibitedWord(Resource):
    #add prohibited word in list
    def put(self,word):
        if gesture_file.addWord(word):
            response = jsonR.copy()
            response['Return'] = True
            response['Message'] = "word added to the list : "+word
            return response
        else:
            response = jsonR.copy()
            response['Return'] = False
            response['Message'] = "Cannot add the word to the list : "+word
            return response

    #search in the list of the word exist
    def get(self,word):
        response = jsonR.copy()
        response['Return'] = False
        response['Message'] = "Get does not exist for this request, you want use put maybe"
        return response

class DeleteProhibitedWord(Resource):
    def put(self,word):
        if gesture_file.deleteWord(word):
            response = jsonR.copy()
            response['Return'] = True
            response['Message'] = "Word deleted from the list : " + word
            return response

class CheckSentence(Resource):
    def put(self):
        print("dedans")
        if 'Sentence' in request.form.keys():
            sentence = request.form['Sentence']
            print("get it")
            newSentence = service.checkSentence(sentence)
            response = jsonR.copy()
            response['Return'] = True
            response['Message'] = "Check Sentence key"
            response['Sentence'] = newSentence
            return response
        else:
            response = jsonR.copy()
            response['Message'] = "The sentence is not in the body. Add the sentence in the key 'Sentence' and resend please"
            response['Return'] = False
            return response


api.add_resource(HelloWorld, '/')
api.add_resource(CleanProhibitedWords, '/administration/clean_list/')
api.add_resource(AddProhibitedWord, '/administration/add_word/<word>/')
api.add_resource(DeleteProhibitedWord, '/administration/delete_word/<word>/')
api.add_resource(CheckSentence, '/service/check_sentence/')
app.run()





#ch = checkSentence("Espece de sale petite pute")
#print(ch)