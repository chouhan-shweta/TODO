from flask import Flask, redirect

app = Flask(__name__)

@app.route('/succes/<name>')
def success(name):
    return 'welcome %s' %name

