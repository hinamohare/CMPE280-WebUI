import os
import uuid

from flask import Flask, render_template, request, json, jsonify, flash
from werkzeug.utils import secure_filename

import api
from bson.json_util import dumps

UPLOAD_FOLDER = './data/images'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg','png'])

app = Flask(__name__)
app.secret_key = "shhhh!!!thisismysecretekey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadimg', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        print("upload called")
        if 'img' not in request.files:
            flash('No file part')
            print("No image included")
            return jsonify( {"result": {"status": "failed - No File Part"}})
            #  return redirect(request.url)
        image = request.files['img']
        print image
        # if user does not select file, browser also
        # submit a empty part without filename
        if image.filename == '':
            flash('No selected file')
            return jsonify({"result": 'no file selected'})
        if image and allowed_file(image.filename):
            filename = str(uuid.uuid4()) +"_" + secure_filename(image.filename)
            #  saveatlocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            saveatlocation = app.config['UPLOAD_FOLDER']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print (filename)
            return jsonify(result ={"imagename": filename})

@app.route("/")
def index():
    return render_template("upload.html")



@app.route("/v1/signup/", methods=['POST'])
def signup():
    try:
        new_art = json.loads(request.data)
        first_name = new_art.get("FirstName")
        last_name = new_art.get("LastName")
        email = new_art.get("Email")
        password = new_art.get("Password")
        contactNo = new_art.get("ContactNo")
        result = api.create_user(first_name, last_name, email, password, contactNo)
        if result is not None:
            return jsonify({"status": "success"}),200
        else:
            return jsonify({"status":"error", "msg": "User already exists"}),404
    except Exception as e:
        print "Signup failed "+str(e)
        return jsonify({"status":"error","msg": "Signup Failed"}), 500

@app.route("/v1/signin/", methods=['POST'])
def signin():
    try:
        user_to_signin = json.loads(request.data)
        email = user_to_signin.get("Email")
        password = user_to_signin.get("Password")
        userInfo = api.get_user(email, password)
        print userInfo
        if userInfo is not None:
            return jsonify({"status": "success","userinfo":json.loads(dumps(userInfo))}), 200
        else:
            return jsonify({"status":"error","msg":"Singin failed. User does not exist"}),404
    except Exception:
        return jsonify({"status":"error","msg": "Singin failed."}), 500

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


@app.route("/v1/art/", methods = ['POST'])
def insertArt():
    try:
        new_art = json.loads(request.data)
        title = new_art.get("Title")
        category = new_art.get("Category")
        description = new_art.get("Description")
        by = new_art.get("By")
        img_name = new_art.get("ImageName")
        result = api.create_art(title, category, description, by, img_name)
        if result is not None:
            return jsonify({"status": "success", "result": result}),200
        else:
            return jsonify({"status":"error", "msg": "Can't insert artwork"}),404
    except Exception as e:
        print "Signup failed "+str(e)
        return jsonify({"status":"error","msg": "create art failed"}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug = True)
