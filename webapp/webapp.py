__author__ = 'alsherman'

from flask import Flask, request, render_template, url_for, redirect, flash
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField, SelectField, StringField
from wtforms.validators import Required
from flask import Markup


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


class Survey(Form):
    q1 = StringField('q1')
    submit = SubmitField('Submit')

@app.route('/index/',  methods=['GET', 'POST'])
def index():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            q1 = form.q1.data

            return render_template('results.html', q1=q1)

    return render_template('index.html', form=form)


@app.route('/index/results/',  methods=['GET', 'POST'])
def results(q1):

    return render_template('results.html', q1=q1)


if __name__ == "__main__":
    app.debug = True
    app.run()
