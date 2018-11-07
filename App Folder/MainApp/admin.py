import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/admin', methods=('GET', 'POST'))
def admin():

	return render_template('/admin/admin.html')

@bp.route('/data', methods=('GET', 'POST'))
def showData():

	db = get_db()

	data = db.execute('SELECT * FROM user').fetchall()
	#@bp.route('/data')
	return render_template('/admin/showData.html', data=data)

	#return render_template('/admin/admin.html')