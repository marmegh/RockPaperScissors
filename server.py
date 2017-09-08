from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    session['wins'] = 0
    session['losses'] = 0
    session['ties'] = 0
    session['plays'] = 0
    session['result'] = 'none'
    return render_template('index.html', wins = session['wins'], losses = session['losses'], ties = session['ties'], plays = session['plays'])
@app.route('/process_play', methods=['POST'])
def process_play():
    print "Got Post Data"
    return render_template('index.html', wins = session['wins'], losses = session['losses'], ties = session['ties'], plays = session['plays'])
app.run(debug=True)
