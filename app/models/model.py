import random
from __future__ import print_function # In python 2.7
import sys

def randomQuestion():
    randomNumber = random.randint(1,3)
    physics = mongo.db.Physics
    randomQuestion = physics.find({'quickID': randomNumber}).next()['Question']
    print(randomQuestion)
randomQuestion()       