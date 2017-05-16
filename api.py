from StringIO import StringIO
from bson import Binary
from model import User, Art
from flask import session, json
from bson.json_util import dumps


"""Error Handler"""

def clarity_error(error):
    """
    
    :param error: 
    :return: 
    """

    return {
        "result": error,
    }

def get_user(email, password):
    """
    
    :param email: 
    :param password: 
    :return: 
    """
    user = User()
    userInfo = user.get_user_details(email, password)
    if userInfo is not None:
        print "Current user id :" + str(userInfo['_id'])
        session['user_id'] = str(userInfo['_id'])
        print "session is set up during signin : " + session['user_id']
        return userInfo
    else:
        return None

def create_user(first_name, last_name, email, password, contactno):
    """
    
    :param first_name: 
    :param last_name: 
    :param email: 
    :param password: 
    :param contactno: 
    :return: 
    """
    user = User()
    userInfo = user.get_user_details(email, password)
    if userInfo is None:
        user_id = user.insertUser(first_name, last_name, email, password, contactno)
        docid = json.loads(user_id)
        session['user_id'] = docid["$oid"]
        print "session is set up during signup : " + session['user_id']
        return "Successfully Added!"
    else:
        return None

def signout_user():
    """

    :return: 
    """
    # remove the username from the session if it is there
    session.pop('user_id', None)
    return

def create_art(title, category, description, img_name):
    """
    extract and convert the image to smaller size and then insert it into database, also insert the id of inserted images into users art array
    :param title: 
    :param category: 
    :param description: 
    :param by: 
    :param img_name: 
    :return: 
    """
    user = session['user_id']
    image = "./data/images/"+img_name
    #binary_image_file = Binary(image_file)  # pymongo libary
    artObj = Art()
    art_id = artObj.insert_art(title, category, description, user, image)
    return  art_id

def retrieve_single_art(art_id):
    artObj = Art()
    art = artObj.get_single_art_details(art_id)
    return art

def retrieve_allArts():
    artsObj = Art()
    artsList = artsObj.get_allArt_details()
    return artsList
