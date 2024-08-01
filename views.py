import json
from flask import Blueprint
from flask import render_template
from flask import request

from tableau import create_tableau
from tableau import tableaus_data
from tableau import tableau_summary
from data import A, b, c

bp = Blueprint('diet-problem', __name__, url_prefix='/')
@bp.route('/')
def index():
    initial_tableau = create_tableau(A, b, c)
    return render_template('index.html', data=tableaus_data, summary=tableau_summary)
