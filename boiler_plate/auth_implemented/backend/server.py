from blueprint_user import user
from blueprint_post import post
from flask import Flask, request
import json

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(post, url_prefix='/post')


# write routes here
@app.route('/')
def home():
    return 'blog post app'


@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,PATCH,DELETE')

    return response 