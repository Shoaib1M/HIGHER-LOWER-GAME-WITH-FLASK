from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDRydGFzenBmc2JzY3d6bGZqMG45aDE1MGRuaG9qc3dudmdyM2tkcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NCOG3Hh4n9fgOB3xmr/giphy.gif" width="200" height="200">'

welcome()


number = random.randint(0,9)

@app.route("/<int:guess>")
def guess(guess):
    if guess == number:
        return '<h1>YOU GOT IT RIGHT!</h1>'\
               '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXphazFmYXcxdGM0eXY3aTM4bzJ4enluam94dnpkM20xdjZjcnA1NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3tTg6UVj3mV6QmgURz/giphy.gif" width="200" height = "200">'
    elif guess > number:
        return '<h1>YOU NEED TO GUESS LOWER</h1>'\
               '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG5vbW5ibGhoZWNodTVzOGkwaWMwY2lkMHduN3d0cDhkczV2eDNueiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g8tLOZ6RWlDvRf5Kfp/giphy.gif" width="200" height = "200">'
    elif guess < number:
        return '<h1>YOU NEED TO GUESS HIGHER</h1>' \
               '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmFqa3BnbHFlMmV6Ynp0NWEyMThrMXNpODBlbHRkaXJ5eDEwbmd1OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1Ll4Pxx3Av5sPd4FcO/giphy.gif" width="200" height = "200">'

guess(number)

if __name__ == "__main__":
    app.run(debug=True)