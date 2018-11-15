# coding=UTF-8

import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.exceptions import abort

bp = Blueprint('wsapi', __name__, url_prefix='/api/1.0')

BASE_DIR = "/media/data"

@bp.before_app_request
def load_logged_in_user():
    pass

@bp.route('/get/data', methods=['POST'])
def get_data_from_pdf():
    response = []
    if request.method == 'POST':
        file_name = request.form['datafile']
        full_path = os.path.join(BASE_DIR, file_name) 
        name, extention = os.path.splitext(file_name) 
        if extention == ".pdf" and os.path.exists(full_path):
            # start to process
            ret = {}
            ret['filename'] = file_name
            ret['heji']     = '123.45'
            ret['ztgz']     = u"钢筋混泥土"
            ret['confident'] = 0.8
            response.append(ret)
            return jsonify(results=response)
        else:
            abort(400, "invalid file name: %s." % file_name)

    