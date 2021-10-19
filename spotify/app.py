'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request
from .models import DB, Song




"""Create and configure an instance of the flask application"""
app = Flask(__name__)



# configure app
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize database
DB.init_app(app)

# create table(s)
with app.app_context():
    DB.create_all()

# ROOT ROUTE
@app.route('/', methods=["GET", "POST"])
def root():     
    """Base view"""
    resp = None
    # When visitor types song and artist then hits a button...
    if request.method == "POST":
        song_name = request.form["song_name"]
        artist_name = request.form["artist_name"]

        song = request.values['song_name']
        artist = request.values['artist_name']

        output=song
        return render_template('predict.html', title = 'home', top_hits = output) 
    else: 
        return render_template('predict.html', title = 'home', top_hits = [])

if __name__ == "__main__":
    app.run()
