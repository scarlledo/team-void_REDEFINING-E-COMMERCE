from flask import Flask, render_template, request
from enquiry import *

app = Flask(__name__)

@app.route('/')
def query():
    return render_template('chat.html')

@app.route('/get')
def show_result():
    userText = request.args.get('msg')
    q = userText.split(' ', 1)[0]
    p = userText.split(' ')[1:]
    item = ' '.join(p)
    if q == 'help':
        result = help()
        return str(result)
    elif q == 'product':
        result = product(item)
        return str(result)
    elif q == 'detail':
        result = detail(item)
        return result
    elif q == 'price':
        result = price(item)
        return result
    elif q == 'hello':
        result = 'Welcome, how can I help you.'
        return result
    else:
        result = 'Please enter the correct keyword, for more type help.'
        return result