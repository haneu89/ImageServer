from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/', methods=['GET'])
def show():
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)