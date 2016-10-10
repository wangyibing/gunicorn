# -*- coding: utf-8 -*-

from flask import Flask, jsonify, session, request

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/', methods=['GET'])
def index():
    return jsonify({'k': 'v'})

@app.route('/test', methods=['GET'])
def test():
    num = request.args.get('num')
    old = session.get('num') or None
    session['num'] = num
    return jsonify({'ret': old})


if __name__ == '__main__':
    print 'Started'
    app.run(host='0.0.0.0')

