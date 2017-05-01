from model import User
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