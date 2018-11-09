# CleanHandymanApp
An app related to the candidate and admin UX for cleaning and handyman related questions.

Hello, this is a WebApp designed to access the required problems. The system-built app would have been a lot static in approach, with more space it has to be allocated in various devices. Web app approach tends to be flexible and can be easily placed into the main server to launch both as an app and also a website. 

Technology stack:
	Python: having a good knowledge of Python programming
	Flask: the web framework used is Flask, adheres well to the flow of the app structure and its database
	SQLite3: a builtin, basic database handler in Python is used, can be easily managed in Python

Name: MainApp
Version: 1.0.0

Developer instruction:
	Download and install Python 3.x.x from www.python.org/downloads
	Install flask in the following way:
		pip install Flask
	Fork this repository 
	Goto Download or Clone and copy the URI for cloning the repository
	Download and install GitBash and GitCMD from https://git-scm.com/downloads
	After installation open GitCMD and type the following command after setting up the proper path of the app
		git clone https://github.com/prcApp/CleanHandymanApp.git
	You can also download ZIP folder and can directly use it.
	After having the stuffs of the repository, goto the folder named App Folder:
		cd App Folder
	Set the flask app settings to the app name "NewApp" by,
		set FLASK_APP=NewApp
	Here, start the flask framework as:
		flask run
	After getting the framework running, goto the browser and type the URL 
		http://127.0.0.1:5000/index
	You'll view the main or home page of the app at this location, consists of links Sign Up and Log In.

Flow of the App:
	Home page has two links Sign Up and Log In
	Clicking Sign Up leads to http://127.0.0.1:5000/signup, user puts in a username, emailid and preference(basically Cleaning, Handyman, Admin)
	Clicking Log In leads to http://127.0.0.1:5000/login, user enters the username as designated in Sign up and emailid. On logging in user with preference Cleaning goes to http://127.0.0.1:5000/cleaning-quiz, with Handyman goes to http://127.0.0.1:5000/handyman-quiz and with the Admin goes to http://127.0.0.1:5000/admin
	In http://127.0.0.1:5000/cleaning-quiz the quiz answers to be typed in the blank space labeled "Answer:". On completing all questions candidate needs to click the "Send Form" button to submit. Candidate is logged out and redirected to the http://127.0.0.1:5000/index.
	Same action with the http://127.0.0.1:5000/handyman-quiz.
	In http://127.0.0.1:5000/admin, the Admin has three choice buttons, "Get Result", "Get Percentile" and "Home".
	"Get Result" shows the overall uptodate data of all the candidates seeking the quiz.
	"Get Percentile" shows the candidate's username and percentile.
	"Home" redirects to http://127.0.0.1:5000/index

