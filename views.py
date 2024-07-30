import json
from flask import Blueprint
from flask import render_template
from flask import request


bp = Blueprint('diet-problem', __name__, url_prefix='/')
@bp.route('/')
def index():
    return render_template('index.html')
