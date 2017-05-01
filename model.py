import pymongo
from bson.json_util import dumps

class User:
    def __init__(self):
        self.dbconnection = pymongo.MongoClient()
        self.dbname = self.dbconnection.cmpe280
        self.collection = self.dbname.user

    def insertUser(self,first_name, last_name, email, password, contactno):
        """
        insert the user information into the user database
        :return: 
        """
        self.post_user_doc = {
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "Password": password,
            "ContactNo": contactno,
            "Art":[]
        }
        user_id = self.collection.insert(self.post_user_doc)
        print user_id
        return dumps(user_id)

    def get_user_details(self, email, password):
        user_doc = self.collection.find_one({"$and" : [{"Email":email},{"Password":password}]})
        if user_doc:
            print "User is present in our database"
            print user_doc
            return user_doc
        else:
            return None


