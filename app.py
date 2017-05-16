import base64
import os
import uuid
from io import BytesIO

import pymongo
from PIL import Image
from flask import Flask, render_template, request, json, jsonify, flash, send_file, url_for, session, g
from werkzeug.utils import secure_filename, redirect

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


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # session['user_id'] ="hina.mohare"
    if request.method == 'POST':
        # check if the post request has the file part
        print("upload called")


        if 'image' not in request.files:
            flash('No file part')
            print("No image included")
            return jsonify( {"result": {"status": "failed - No File Part"}})
            #  return redirect(request.url)
        image = request.files['image']
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
            title = request.form.get("Title")
            category = request.form.get("Category")
            description = request.form.get("Description")
            result = api.create_art(title, category, description, filename)
            return redirect(url_for('index'))
    return  render_template ("upload.html")

@app.route("/")
def index():
    name = request.args.get('name')
    print ("name : ", name)
    return  render_template ("index.html", username = name)

@app.route("/checklogin",methods=['GET'])
def checklogin():
    try:
        if session['user_id'] is not None:
            return jsonify({"isloggedin": True})
        return jsonify({"isloggedin": False})
    except Exception:
        return jsonify({"isloggedin": False})


@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        #new_art = json.loads(request.data)
        first_name = request.form.get("FirstName")
        last_name = request.form.get("LastName")
        email = request.form.get("Email")
        password = request.form.get("Password")
        contactNo = request.form.get("ContactNo")
        result = api.create_user(first_name, last_name, email, password, contactNo)
        if result is not None:
            name = first_name+" "+last_name
            print ("Loggedin user name is:", name)
            return redirect(url_for('index', name = name))
        else :
            return render_template ("signup.html")

        # don't need to test request.method == 'GET'
    return  render_template ("signup.html")

@app.route("/signin", methods=['POST','GET'])
def getsignin():
    if request.method == 'GET':
        return  render_template ("signin.html")
    try:
        print("sign in called")
        email = request.form.get("email")
        password = request.form.get("password")
        userInfo = api.get_user(email, password)
        if userInfo is not None:
            name = userInfo["FirstName"]+" "+userInfo["LastName"]
            print ("Loggedin user name is:", name)
            return redirect(url_for('index', name = name))
        else:
            print ('{"status":"error","msg":"Singin failed. User does not exist"}')
            return redirect(url_for('getsignin'))
    except Exception:
        return render_template("signin.html")

# @app.route("/signup1", methods=['POST'])
# def signup1():
#     try:
#         # new_art = json.loads(request.data)
#         # first_name = new_art.get("FirstName")
#         # last_name = new_art.get("LastName")
#         # email = new_art.get("Email")
#         # password = new_art.get("Password")
#         # contactNo = new_art.get("ContactNo")
#         # result = api.create_user(first_name, last_name, email, password, contactNo)
#         return redirect(url_for('index', sessionid=result.id))
#
#     except Exception as e:
#         print "Signup failed "+str(e)
#         return render_template("signup.html")
#


@app.route("/logout", methods=['GET'])
def signout():
    """
    
    :return: 
    """

    try:
        api.signout_user()
        return redirect(url_for('index'))
    except Exception as e:
        print "signout failed " + str(e)
        return redirect(url_for('index'))



def insertArt(title,category,description,imagename):
    try:

        new_art = json.loads(request.data)
        title = new_art.get("Title")
        category = new_art.get("Category")
        description = new_art.get("Description")
        #by = new_art.get("By")
        img_name = new_art.get("ImageName")
        result = api.create_art(title, category, description,img_name)
        if result is not None:
            return jsonify({"status": "success", "result": result}),200
        else:
            return jsonify({"status":"error", "msg": "Can't insert artwork"}),404

    except Exception as e:
        print "Signup failed "+str(e)
        return jsonify({"status":"error","msg": "create art failed"}), 500

@app.route('/v1/art/<art_id>', methods = ['GET'])
def retrieveArt(art_id):
    result = api.retrieve_single_art(art_id)
    return jsonify({"result":result})


# dbconnection = pymongo.MongoClient()
# dbname = dbconnection.cmpe280



@app.route('/v1/arts/', methods = ['GET'])
def retrieve_image():
    result = api.retrieve_allArts()
    return jsonify({"result":result})
    # data = dbname.art.find_one()
    # data1 = json.loads(dumps(data))
    # img = data1['Image']
    # #img1 = img['Image']
    # decode=img.decode()
    # i = Image.open(decode)
    # return i
    # img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
    # description_tag = "<p>Title : "+data1["Title"]+" <br>User : "+data1["User"] + img_tag
    # return description_tag

# g.name = ""
# @app.context_processor
# def inject_user():
#     return dict(name=g.name)
#
# @app.context_processor
# def inject_user():
#     return dict(name=g.name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug = True)