from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecured"
@app.route('/')
def start():
    return render_template('start.html', count=session['count'])
@app.route('/process', methods=['POST'])
def reload_And_Reset(): 
    if request.form['action']=='reload':
        session['count'] =session['count']+2
        print session['count']
    if request.form['action']=='reset':
        session['count']=1
        print session['count']
    return redirect('/')
app.run(debug=True)
