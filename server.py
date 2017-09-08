from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    session['wins'] = 0
    session['losses'] = 0
    session['ties'] = 0
    session['plays'] = 0
    session['result'] = 'none'
    session['computer_choice'] = 'none'
    session['computer'] = 'none'
    session['user'] = 'none'
    return render_template('index.html', wins = session['wins'], losses = session['losses'], ties = session['ties'], plays = session['plays'], result = session['result'], comp_choice = session['computer_choice'], computer = session['computer'], user = session['user'])
@app.route('/process_play', methods=['POST'])
def process_play():
    session['wins'] = session['wins'] + 0
    session['losses'] = session['losses'] + 0
    session['ties'] = session['ties'] + 0
    session['plays'] = session['plays'] + 1
    comp_choice = random.randint(0,2)
    if comp_choice == 0:
        session['computer'] = 'rock'
    elif comp_choice == 1:
        session['computer'] = 'paper'
    elif comp_choice ==2:
        session['computer'] = 'scissors'
    session['user'] = request.form['user_choice']
    if session['computer'] == session['user']:
        session['result'] = 'tie'
        session['ties'] = session['ties'] + 1
    elif session['computer'] == 'rock' and session['user'] == 'paper':
        session['result'] = 'win'
        session['wins'] = session['wins'] + 1
    elif session['computer'] == 'paper' and session['user'] == 'scissors':
        session['result'] = 'win'
        session['wins'] = session['wins'] + 1
    else:
        session['result'] = 'lose'
        session['losses'] = session['losses'] + 1
    print "Got Post Data"
    return render_template('index.html', wins = session['wins'], losses = session['losses'], ties = session['ties'], plays = session['plays'], result = session['result'], comp_choice = session['computer_choice'], computer = session['computer'], user = session['user'])
app.run(debug=True)
