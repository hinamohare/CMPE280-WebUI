import base64
from StringIO import StringIO
from PIL import Image

import pymongo
from bson import Binary, ObjectId
from bson.json_util import dumps
from flask import json

dbconnection = pymongo.MongoClient()
dbname = dbconnection.cmpe280

def getdbconn():
    return dbname;

class User:
    def __init__(self):
        self.dbname = getdbconn()
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
            "Arts":[]
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

    def add_artInUserAccount(self, user_id, art_id):
        pass


class Art:
    def __init__(self):
        self.dbname = getdbconn()
        self.collection = self.dbname.art

    def insert_art(self, title, category, description, user, image):
        im = Image.open(image)
        imResize = im.resize((500, 500), Image.ANTIALIAS)
        imResize.save("test.jpg", 'JPEG', quality=90)
        image_file = open('test.jpg', 'rb')
        encoded_string = base64.b64encode(image_file.read())
        # print encoded_string
        #abc = dbname.art.insert({"image": encoded_string})
        #print ("inserted")
        self.post_art_doc = { "Title" : title, "Category": category, "Description": description, "User": user, "Image" : encoded_string}
        art_id = self.collection.insert(self.post_art_doc)
        print art_id
        return dumps(art_id)

    def get_single_art_details(self, art_id):
        art = self.collection.find_one({"_id": ObjectId(art_id)})

        if art is not None:
            art_doc = json.loads(dumps(art))

            new_art = {}
            img = art_doc['Image']
            # img1 = img['Image']
            decode = img.decode()
            new_art["image_src"] = "data:image/png;base64,{0}".format(decode)
            new_art["Title"] = art_doc["Title"]
            new_art["Category"] = art_doc["Category"]
            new_art["Description"] = art_doc["Description"]
            new_art["User"] = art_doc["User"]
            new_art["id"] = art_doc["_id"]
            return new_art
        else:
            return None

    def get_allArt_details(self):
        arts = self.collection.find().sort("_id",-1)
        print arts.count
        if arts.count > 0:
            art_docs = json.loads(dumps(arts))
            art_list = []
            for art in art_docs:
                new_art = {}
                img = art['Image']
                # img1 = img['Image']
                decode = img.decode()
                new_art["image_src"] = "data:image/png;base64,{0}".format(decode)
                new_art["Title"] = art["Title"]
                new_art["Category"] = art["Category"]
                new_art["Description"] = art["Description"]
                new_art["User"] = art["User"]
                new_art["id"] = art["_id"]
                art_list.append(new_art)
                #print new_art["id"]
            return art_list
        else:
            return None


# obj = Art()
# obj.insert_art("Home1","Craft","FairyHourse","Hina","./data/images/95c88d82-afe0-4368-9c3c-09c6f221c79e_IMG_4438.jpg")
# obj.insert_art("Home2","Craft","FairyHourse","Tona","./data/images/IMG_4432.jpg")
# obj.insert_art("Home3","Craft","FairyHourse","Viyona","./data/images/IMG_4443.jpg")

# def retrieve_image():
#     arts = dbname.art.find()
#     print arts.count
#     art_docs = json.loads(dumps(arts))
#     art_list = []
#     for art in art_docs:
#         new_art = {}
#         img = art['Image']
#         # img1 = img['Image']
#         decode = img.decode()
#         new_art["image_src"] = "data:image/png;base64,{0}".format(decode)
#         new_art["Title"] = art["Title"]
#         new_art["Category"] = art["Category"]
#         new_art["Description"] = art["Description"]
#         new_art["User"] = art["User"]
#         new_art["id"] = art["_id"]
#         art_list.append(new_art)
#         print new_art["id"]
#     #return art_list
#     #print art_list
#
# retrieve_image()



# image_file = StringIO(open("./data/images/95c88d82-afe0-4368-9c3c-09c6f221c79e_IMG_4438.jpg",'rb').read())
# Binary_image_file = Binary(bytes(image_file)) #pymongo libary
#obj = Art()
# obj.insert_art("Viyona","Painting","Abstract","hina",Binary_image_file)

# Stringio_image_file = dbname.art.find_one({"_id": ObjectId("5917d570b61e12119c9aca69")})
# image_data = StringIO(Stringio_image_file)
# image = Image.

# def insert_image():
#     #with open("./data/images/IMG_4432.jpg", "rb") as image_file:
#     im = Image.open("./data/images/IMG_4432.jpg")
#     imResize = im.resize((200, 200), Image.ANTIALIAS)
#     imResize.save("test.jpg", 'JPEG', quality=90)
#     image_file = open('test.jpg', 'rb')
#     encoded_string = base64.b64encode(image_file.read())
#     #print encoded_string
#     art_id = dbname.art.insert({"image":encoded_string})
#     print ("inserted")
#
#
# insert_image()
#insert_image()

# def resize():
# for item in dirs:
# if os.path.isfile(path+item):
# im = Image.open(path+item)
# f, e = os.path.splitext(path+item)
# imResize = im.resize((200,200), Image.ANTIALIAS)
# #output = StringIO.StringIO()
# imResize.save("test.jpg", 'JPEG', quality=90)
# image_file = open('test.jpg', 'rb')
# encoded_string = base64.b64encode(image_file.read())
# print encoded_string
# abc = artcoll.insert({"image": encoded_string})
# print ("inserted")