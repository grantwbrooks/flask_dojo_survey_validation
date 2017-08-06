from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_name():

    name = request.form['yourname']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print request.form

    if len(request.form['yourname']) < 1:
        flash("Name cannot be blank!")
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!")
    if len(request.form['comment']) > 120:
        flash("Comment cannot be so HUGE!")

# The line below is key so you get all of the error messages to display on the first page
    if '_flashes' in session:
        return redirect('/')
    else:
        return render_template('result.html', name=name, location=location, language=language, comment=comment )


app.run(debug=True)