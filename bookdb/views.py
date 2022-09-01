from flask import Blueprint
from flask import render_template, request




views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h2>Home Page</h2>"