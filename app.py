from flask import Flask, send_file, request, json, jsonify
import api
from bson.json_util import dumps

app = Flask(__name__)
app.secret_key = "shhhh!!!thisismysecretekey"


@app.route("/")
def index():
    return send_file("templates/index.html")



@app.route("/v1/signup/", methods=['POST'])
def signup():
    try:
        new_user = json.loads(request.data)
        first_name = new_user.get("FirstName")
        last_name = new_user.get("LastName")
        email = new_user.get("Email")
        password = new_user.get("Password")
        contactNo = new_user.get("ContactNo")
        result = api.create_user(first_name, last_name, email, password, contactNo)
        if result is not None:
            return "Success",200
        else:
            return jsonify({"error": "User already exists"}),404
    except Exception as e:
        print "Signup failed "+str(e)
        return jsonify({"error": "Signup Failed"}), 500

@app.route("/v1/signin/", methods=['POST'])
def signin():
    try:
        user_to_signin = json.loads(request.data)
        email = user_to_signin.get("Email")
        password = user_to_signin.get("Password")
        userInfo = api.get_user(email, password)
        print userInfo
        if userInfo is not None:
            return jsonify({"user":json.loads(dumps(userInfo))}), 200
        else:
            return jsonify({"error":"Singin failed. User does not exist"}),404
    except Exception:
        return jsonify({"error": "Singin failed."}), 500

@app.route("/v1/signout/", methods=['POST'])
def signout():
    """
    
    :return: 
    """
    try:
        api.signout_user()
        return "success",200
    except Exception as e:
        print "signout failed " + str(e)
        return jsonify({"error": "Signout Failed"}), 500



if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug = True)