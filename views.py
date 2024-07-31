import json
from flask import Blueprint
from flask import render_template
from flask import request

from tableau import create_tableau, A, b, c

bp = Blueprint('diet-problem', __name__, url_prefix='/')
@bp.route('/')
def index():
    initial_tableau = create_tableau(A, b, c)
    return render_template('index.html', tableau=initial_tableau)
