from flask import Flask, render_template, request, jsonify

app_post = Flask(__name__)


@app_post.route('/')

def post(id):

    if id == 1:
        return jsonify('Hi!')
    
    if id == 2:
        return jsonify('Hi!!!!!!!!!!!!!!!!')







