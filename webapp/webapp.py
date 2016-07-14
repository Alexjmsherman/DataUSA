__author__ = 'alsherman'

from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms.fields import SubmitField, StringField
from wtforms.validators import Required
import occupation_prediction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


class Survey(Form):
    q1 = StringField('q1', validators=[Required()])
    q2 = StringField('q2', validators=[Required()])
    q3 = StringField('q3', validators=[Required()])
    q4 = StringField('q4', validators=[Required()])
    q5 = StringField('q5', validators=[Required()])

    submit = SubmitField('Submit')

@app.route('/index/',  methods=['GET', 'POST'])
def index():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            q1 = form.q1.data
            q2 = form.q2.data
            result = occupation_prediction.predict(prediction=[q1,q2])

            return render_template('results.html', q1=result)

    return render_template('index.html', form=form)


@app.route('/index/results/',  methods=['GET', 'POST'])
def results(q1):

    return render_template('results.html', q1=q1)


if __name__ == "__main__":
    app.debug = True
    app.run()
