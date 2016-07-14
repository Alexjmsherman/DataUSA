__author__ = 'alsherman'

from flask import Flask, request, render_template, url_for, redirect, flash
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField, SelectField, StringField
from wtforms.validators import Required
from whoosh_search import search
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database_setup import SectionTable
from flask import Markup


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


class Survey(Form):
    q1 = SelectField('q1', validators=[Required()])
    q2 = SelectField('q2', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/index/',  methods=['GET', 'POST'])
def index():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            query = form.search.data
            q1 = form.q1.data
            q2 = form.q2.data

            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
