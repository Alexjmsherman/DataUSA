__author__ = 'alsherman'

from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms.fields import SubmitField, StringField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import Required, NumberRange
import occupation_prediction
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
occupation_prediction = occupation_prediction.predictive_models()

class Survey(Form):
    # q1 = StringField('q1', validators=[Required()])
    q1 = IntegerRangeField('q1', default=1, validators=[NumberRange(min=1, max=5)])
    q2 = IntegerRangeField('q2', default=1, validators=[NumberRange(min=1, max=5)])
    q3 = IntegerRangeField('q3', default=1, validators=[NumberRange(min=1, max=5)])
    q4 = IntegerRangeField('q4', default=1, validators=[NumberRange(min=1, max=5)])
    q5 = IntegerRangeField('q5', default=1, validators=[NumberRange(min=1, max=5)])

    submit = SubmitField('Submit')

@app.route('/index/',  methods=['GET', 'POST'])
def index():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            q1 = form.q1.data
            q2 = form.q2.data
            q3 = form.q3.data
            q4 = form.q4.data
            q5 = form.q5.data

            prediction_data = [q1,q2,q3,q4,q5]

            _result = occupation_prediction.predict(prediction=prediction_data)
            result = _result.values

            vals=[]
            for ind, row in _result.iterrows():
                val = {'cip':row[0] , 'prob':row[1], 'name_long':row[2]}
                vals.append(val)

            skills_data = [{'skill':'Reading Comprehension','cip':'2.A.1.a','user_input':q1},
                            {'skill':'Active Listening','cip':'2.A.1.b','user_input':q2},
                            {'skill':'Writing','cip':'2.A.1.c','user_input':q3},
                            {'skill':'Speaking','cip':'2.A.1.d','user_input':q4},
                            {'skill':'Mathematics','cip':'2.A.1.e','user_input':q5}]

            return render_template('results.html', result=result, vals=json.dumps(vals), skills_data=json.dumps(skills_data))

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.debug = True
    app.run()


'''

class TestForm(Form):
    age = IntegerRangeField('Age', default=1, validators=[NumberRange(min=1, max=5)])

@app.route('/test/',  methods=['GET', 'POST'])
def test():
    form = TestForm()
    return render_template('test.html', form=form)
'''