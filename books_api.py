from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from pymongo import ALL, MongoClient
from pymongo.message import query
from query import db_query, db_full_query, parse

app = Flask(__name__)
api = Api(app)



class Status(Resource):
# Class for getting the status for all of the books in the books collection
    def get(self):
        #from query import db_query
        return db_query()

class RetrieveID(Resource):            
    def get(self, book_id):    
        client = MongoClient("mongodb+srv://kirjastoAdmin:<password>@cluster0.6se1s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['kirjasto-backend']
        collection = db['backendAPI']
        retrievedID = list(collection.find({'Book ID' : book_id,}, {
             '_id': False
            }))
        return retrievedID

class Books(Resource):
# Class for getting the details of all of the books in the books collection
    def get(self):
        return db_full_query()

class Loan (Resource):
# Class for manipulating the loaning system for the books in the books collection
    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', required = True)
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        parser.add_argument('loaner', required = True)
        parser.add_argument('loan_status', required = True)
        
        args = parser.parse_args()
        # Checking if the book name already exists.        
        client = MongoClient("mongodb+srv://kirjastoAdmin:<password>@cluster0.6se1s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['kirjasto-backend']
        collection = db['backendAPI']
        # had to make _id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        #iterate through retrieved and find if post value "name" is the same as database value Name.
        #if true -> update. else throw errors.
        for name in retrieved:
            if args['name'] in name['Name']:
                new_book = collection.find_one_and_update(name,{"$set": parse()})
            elif args['name'] not in name['Name']:
                return {'message': f"'{args['name']}' doesnt exist."
                }, 401
            else:
                return {
                     'message': f" Unknown error."
                }, 401
            

        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
"""     Shelved for V2++
    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', required = True)
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        parser.add_argument('loaner', required = True)
        parser.add_argument('loan_status', required = True)
        
        args = parser.parse_args()
        # Checking if the book name already exists.        
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['books']
        # had to make _id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        
        for name in retrieved:

            if args['name'] in name['Name']:
                return {
                     'message': f"'{args['name']}' already exists."
                }, 401
        else:
            db_query()
            new_book = collection.insert_one(parse())    

    def put(self):
        return 401

    def delete(self):
       # Require these args for the DELETE request.

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['books']
        removeBook = collection.find_one_and_delete(parse())    
        return db_query(), 200
        

    def push(self):
        return 401 """

# Class for interacting with comments collection
class Comments(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['comments']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)

        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['comments']
        new_book = collection.insert_one({
            'Commenter' : args['commenter'],
            'Message' : args['message'],     
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)

        args = parser.parse_args()

        if args['name'] in list(collection['Name']):
            client = MongoClient('localhost', 27017)
            db = client['Laiberi']
            collection = db['booksAvail']
            updateBook = collection.find_one_and_replace({
                'Commenter' : args['commenter'],
                'Message' : args['message'],     
        })    

        retrieved = list(collection.find({}, {'_id' : False}))


        return retrieved, 200

    def delete(self):
    # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('commenter', required = True)
        parser.add_argument('message', required = True)
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Laiberi']
        collection = db['booksAvail']
        removeBook = collection.find_one_and_delete({
            'Commenter' : args['commenter'],
            'Message' : args['message'],          
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401

api.add_resource(Status, '/status') 
api.add_resource(RetrieveID, '/status/<book_id>')
api.add_resource(Books, '/books')
api.add_resource(Loan, '/loan')
api.add_resource(Comments, '/comments')


# Runs on port 8080!!
if __name__ == "__main__":
    app.run( debug = True, host='127.0.0.1', port=8000 )