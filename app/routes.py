from __future__ import print_function # In python 2.7
import sys, random
from app import app
from flask import render_template, request, redirect, url_for
# from models import model, formopener
from flask_pymongo import PyMongo
app.config['MONGO_DBNAME'] = 'RegentsDB'
app.config['MONGO_URI'] = 'mongodb+srv://stfarrell:iliketurtles@cluster0-vk0xc.mongodb.net/RegentsDB?retryWrites=true&w=majority'
mongo = PyMongo(app)



@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')
    
    
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('/')
    else:
        username = request.form['username']
        password = request.form['password']
        
        users = mongo.db.Users
        if username == users.find({'username': username}).next()['username']:
            return 'That user already exists!'
        else:
            users.insert({'username': username, 'password': password})
            return redirect('/')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/')
    else:
        username = request.form['username']
        password = request.form['password']
        
        users = mongo.db.Users
        print(users.find({'username': username}).next()['username'], file=sys.stderr)

        if (username == users.find({'username': username}).next()['username']) and (password == users.find({'password': password}).next()['password']):
            return render_template('physics.html', username = username)
        else:
            return 'There is no user with that combination of username and password!'
            
@app.route('/physics/question', methods=['GET', 'POST'])
def question():
    randomNumber = random.randint(1,10)
    physics = mongo.db.Physics
    print('RANDOM NUMBER IS ', randomNumber, file=sys.stderr)
    randomQuestion = physics.find({'QuickID': randomNumber}).next()['Question']
    print(randomQuestion, file=sys.stderr)
    randomVid = physics.find({'QuickID': randomNumber}).next()['Video']
    print(randomVid, file=sys.stderr)
    randomAns = physics.find({'QuickID': randomNumber}).next()['Answer']
    return render_template('physicsQuestion.html', randomQuestion=randomQuestion, randomVid=randomVid, randomAns=randomAns)
    
    
