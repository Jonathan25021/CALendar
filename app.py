from flask import Flask, request, render_template

#import firebase_admin
#from firebase_admin import credentials

#cred = credentials.Certificate("<filename.json>")
#firebase_admin.initialize_app(cred)
#db = firestore.client()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signIn")
def signIn():
    return render_template('signIn.html')

@app.route("/calendar")
def calendar():
    return render_template('calendar.html')

@app.route("/toDoList")
def toDoList():
    return render_template('toDoList.html')

@app.route("/accountInfo")
def accountInfo():
    return render_template('accountInfo.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)