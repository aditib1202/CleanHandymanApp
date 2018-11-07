import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('candidate', __name__, url_prefix='/candidate')

@bp.route('/cleaning', methods=('GET', 'POST'))
def cleaning():

	return render_template('/candidate/cleaning.html')

@bp.route('/handyman', methods=('GET', 'POST'))
def handyman():

	return render_template('/candidate/handyman.html')

'''@bp.route('/data', methods=('GET', 'POST'))
def showData():

	db = get_db()

	data = db.execute('SELECT * FROM user').fetchall()
	#@bp.route('/data')
	return render_template('/admin/showData.html', data=data)

	#return render_template('/admin/admin.html')'''