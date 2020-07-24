from flask import Flask,request,render_template,jsonify
import requests
from pos_tag import *

# Creating app instance
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/get_pos', methods=['GET','POST'])
def POS():
    if(request.method == 'POST'):
        text = request.get_json()['text']
        return pos_obj.result(text)
    else:
        return jsonify({'error': 'Text not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)   