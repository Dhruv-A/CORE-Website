from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
  return render_template('home.html')

@app.route('/courses')
def coursepage():
  return render_template('courses.html')

@app.route('/python/<int:postID>')
def pyTutorial(postID):
  if postID == 1:
    return render_template('pyT1.html')
  elif postID == 2:
    return render_template('pyT2.html')
  elif postID == 3:
    return render_template('pyT3.html')
  elif postID == 4:
    return render_template('pyT4.html')
  else:
    return '<h1>Page Not Found</h1>'

@app.route('/about')
def aboutpage():
  return render_template('about.html')

@app.route('/contact')
def contactpage():
  return render_template('contact.html')


app.run(host='0.0.0.0')