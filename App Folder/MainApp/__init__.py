#from flask import Flask
import sqlite3
import functools

from flask import (
	Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

#conn = sqlite3.connect('Database.db')

#conn.execute('CREATE TABLE marks3 (username TEXT, preference TEXT, total INTEGER, percentile INTEGER)')
#conn.execute('CREATE TABLE userSign2 (username TEXT, emailid TEXT, preference TEXT)')
#conn.execute('CREATE TABLE marks (total INTEGER)')
#conn.execute('CREATE TABLE userSign1 (username TEXT, emailid TEXT, preference TEXT, total INTEGER)')
#conn.execute('CREATE TABLE quizDb2 (username TEXT, emailid TEXT, total INTEGER)')
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/index')
def index():
	return render_template('/index/index.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
	if(request.method == 'POST'):
		username = request.form['username']
		emailid = request.form['emailid']
		preference = request.form['preference']

		selectUser, selectPref = username, preference
		#select = format(preference)
		marks = -1

		with sqlite3.connect("Database.db") as con:
			cur = con.cursor()
			cur.execute('INSERT INTO userSign2 (username, emailid, preference) VALUES (?, ?, ?)', 
				(username, emailid, preference))
			con.commit()

		return redirect(url_for('login'))
	return render_template('/user/signup.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
	if(request.method == 'POST'):
		username = request.form['username']
		emailid = request.form['emailid']
		marks, percentile = -1, -1
		with sqlite3.connect("Database.db") as con:
			cur = con.cursor()
			preference = cur.execute('SELECT preference FROM userSign2 WHERE emailid=?',(emailid,)).fetchone()
			preference1 = cur.execute('SELECT preference FROM marks3 WHERE username=?',(username,)).fetchone()
			if(preference[0] == 'Admin'):
				pass
			else: 
				if(preference1 is None):
					cur.execute('INSERT INTO marks3 (username, preference, total, percentile) VALUES (?, ?, ?, ?)',
								(username, preference[0], marks, percentile,)
						)
				else:
					cur.execute('UPDATE marks3 SET total=? WHERE username=?',(marks,username,))
					cur.execute('UPDATE marks3 SET percentile=? WHERE username=?',(percentile,username,))
			con.commit()

		#selectUser, selectPref = username, preference[0]
		if(preference[0] == 'Cleaning'):
			return redirect(url_for('cleaning'))
		if(preference[0] == 'Handyman'):
			return redirect(url_for('handyman'))
		if(preference[0] == 'Admin'):
			return redirect(url_for('admin'))

	return render_template('/user/login.html')

@app.route('/cleaning-quiz', methods=('GET', 'POST'))
def cleaning():
	if(request.method == 'POST'):
		answer1 = request.form['answer1']
		answer2 = request.form['answer2']
		answer3 = request.form['answer3']
		answers = [answer1, answer2, answer3]
		correct = ['c', 'c', 'b']
		marks = 0
		marks = int(marks)
		for index in range(0, len(correct)):
			if(answers[index] == correct[index]):
				marks += 1
		with sqlite3.connect("Database.db") as con:
			cur = con.cursor()
			#cur.execute('SELECT username FROM userSign2')
			cur.execute('UPDATE marks3 SET total=? WHERE total=-1',(marks,))
			con.commit()
		return redirect(url_for('index'))
	return render_template('/quiz/cleaning.html')

@app.route('/handyman-quiz', methods=('GET', 'POST'))
def handyman():
	if(request.method == 'POST'):
		answer1 = request.form['answer1']
		answer2 = request.form['answer2']
		answers = [answer1, answer2]
		correct = ['a', 'c']
		marks = 0
		marks = int(marks)
		for index in range(0, len(correct)):
			if(answers[index] == correct[index]):
				marks += 1
		with sqlite3.connect("Database.db") as con:
			cur = con.cursor()
			#cur.execute('SELECT username FROM userSign2')
			cur.execute('UPDATE marks3 SET total=? WHERE total=-1',(marks,))
			con.commit()
		return redirect(url_for('index'))
	return render_template('/quiz/handyman.html')

@app.route('/admin', methods=('GET', 'POST'))
def admin():
	if(request.method == 'POST'):
		return redirect(url_for('index'))
	return render_template('/admin/admin.html')

@app.route('/data', methods=('GET', 'POST'))
def showData():
	with sqlite3.connect("Database.db") as con:
		cur = con.cursor()
		data = cur.execute('SELECT username, preference, total FROM marks3').fetchall()
	return render_template('/admin/showData.html', data=data)

@app.route('/percentile', methods=('GET', 'POST'))
def showPercentile():
	percentile = 0
	with sqlite3.connect("Database.db") as con:
		cur = con.cursor()
		marks = cur.execute('SELECT total FROM marks3').fetchone()
		print(marks[0])
		totalRows = cur.execute('SELECT Count(*) FROM marks3').fetchone()
		lesserRows = cur.execute('SELECT Count(total) FROM marks3 WHERE total<?',(int(marks[0]),))
		#print(totalRows[0], lesserRows[0])
		#percentile = (int(lesserRows[0])/int(totalRows[0]))*100
		cur.execute('UPDATE marks3 SET percentile=? WHERE percentile=-1',(percentile,))
		data = cur.execute('SELECT * FROM marks3')
		#con.commit()
	return render_template('/admin/showPercentile.html', data=data)


if __name__=='__main__':
	app.run(debug=True)