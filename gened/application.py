import os
import re
import datetime

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# handles internal server errors
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    flash("INTERNAL SERVER ERROR: 500", 'danger')
    return redirect("/")


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


################################################################## Opening Page ##################################################################


# takes users to the homepage
@app.route("/")
def home():
    """Shows opening page"""
    return render_template("quiz.html")



################################# Calculator #################################


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """find director that most matches quiz taker"""
    quiztaker = []
    print(quiztaker)
    if request.method == "POST":

        # ensure user inputs information
        if not request.form.get("superpower") and not request.form.get("home") and not request.form.get("color") and not request.form.get("lists") and not request.form.get("personality") and not request.form.get("phone"):
            flash("no input", 'danger')

        # quiz questions
        if request.form.get("superpower"):
            if request.form.get("superpower") == "Invisibility":
                quiztaker.append("wkw")

            elif request.form.get("superpower") == "The ability to fly":
                quiztaker.append("lee")

            elif request.form.get("superpower") == "Create money out of thin air":
                quiztaker.append("bong")

            else:
                quiztaker.append("ozu")

        # if a person doesn't input any personal info, the data is 0
        else:
            quiztaker.append("NA")

        if request.form.get("home"):
            if request.form.get("home") == "Hang up your coat and put your shoes on your neatly-organized rack":
                quiztaker.append("lee")

            elif request.form.get("home") == "Immediately nap":
                quiztaker.append("ozu")

            elif request.form.get("home") == "Go straight for the fridge":
                quiztaker.append("bong")

            else:
                quiztaker.append("wkw")

        # if a person doesn't input any personal info, the data is 0
        else:
            quiztaker.append("NA")

        if request.form.get("color"):
            if request.form.get("color") == "Purple":
                quiztaker.append("bong")

            elif request.form.get("color") == "Green":
                quiztaker.append("lee")

            elif request.form.get("color") == "Red":
                quiztaker.append("wkw")

            else:
                quiztaker.append("ozu")

        # if a person doesn't input any personal info, the data is 0
        else:
            quiztaker.append("NA")

        if request.form.get("lists"):
            if request.form.get("lists") == "Yes":
                quiztaker.append("lee")

            elif request.form.get("lists") == "No":
                quiztaker.append("wkw")

            elif request.form.get("color") == "Only if I’m busy":
                quiztaker.append("ozu")

            else:
                quiztaker.append("bong")

        # if a person doesn't input any personal info, the data is 0
        else:
            quiztaker.append("NA")

        if request.form.get("personality"):
            if request.form.get("personality") == "Optimistic":
                quiztaker.append("ozu")

            elif request.form.get("personality") == "Pessimistic":
                quiztaker.append("bong")

            elif request.form.get("personality") == "Realistic":
                quiztaker.append("wkw")

            else:
                quiztaker.append("lee")

        if request.form.get("phone"):
            if request.form.get("phone") == "Scrolling through TikTok":
                quiztaker.append("bong")

            elif request.form.get("phone") == "Color coding your calendar":
                quiztaker.append("lee")

            elif request.form.get("phone") == "Coming up with a caption for the perfect insta post":
                quiztaker.append("wkw")

            else:
                quiztaker.append("ozu")

        # if a person doesn't input any personal info, the data is 0
        else:
            quiztaker.append("NA")


        print(quiztaker)
        answer = max(set(quiztaker), key = quiztaker.count)
        print (answer)

        #  sends user to the end page
        if answer == "wkw":
            return render_template("wkw.html")
        elif answer == "lee":
            return render_template("lee.html")
        elif answer == "ozu":
            return render_template("ozu.html")
        elif answer == "bong":
            return render_template("bong.html")
        else:
            return redirect("/homepage")

    else:

        # the GET method which presents the user with the form
        return render_template("quiz.html")
