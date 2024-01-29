from flask import Flask, render_template
import bibtexparser
import os


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/implementation')
def implementation():
    return render_template('implementation.html')


@app.route('/publications')
def publications():
    return render_template('publications.html')


@app.route('/field_campaigns')
def field_campaigns():
    return render_template('activities/field_campaigns.html')


@app.route('/analysis')
def analysis():
    return render_template('activities/analysis.html')


@app.route('/volres')
def volres():
    return render_template('activities/volres.html')


@app.route('/data_rescue')
def data_rescue():
    return render_template('activities/data_rescue.html')


@app.route('/modeling')
def modeling():
    return render_template('activities/modeling.html')


@app.route('/meetings')
def meetings():
    return render_template('meetings.html')


if __name__ == '__main__':
    app.run()
