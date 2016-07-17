__author__ = 'alsherman'

import json

from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms.fields import SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange
from modules.occupation_prediction import PredictiveModels
from modules.data_usa_names_and_ids import DataUsaNamesAndIds


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
names_and_ids = DataUsaNamesAndIds()
occupation_prediction = PredictiveModels(names_and_ids)


class Survey(Form):
    """ Survey questions including all skills for a user to provide personal ratings  """
    q0 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][0], default=1, validators=[NumberRange(min=1, max=5)])
    q1 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][1], default=1, validators=[NumberRange(min=1, max=5)])
    q2 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][2], default=1, validators=[NumberRange(min=1, max=5)])
    q3 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][3], default=1, validators=[NumberRange(min=1, max=5)])
    q4 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][4], default=1, validators=[NumberRange(min=1, max=5)])
    q5 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][5], default=1, validators=[NumberRange(min=1, max=5)])
    q6 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][6], default=1, validators=[NumberRange(min=1, max=5)])
    q7 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][7], default=1, validators=[NumberRange(min=1, max=5)])
    q8 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][8], default=1, validators=[NumberRange(min=1, max=5)])
    q9 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][9], default=1, validators=[NumberRange(min=1, max=5)])
    q10 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][10], default=1, validators=[NumberRange(min=1, max=5)])
    q11 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][11], default=1, validators=[NumberRange(min=1, max=5)])
    q12 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][12], default=1, validators=[NumberRange(min=1, max=5)])
    q13 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][13], default=1, validators=[NumberRange(min=1, max=5)])
    q14 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][14], default=1, validators=[NumberRange(min=1, max=5)])
    q15 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][15], default=1, validators=[NumberRange(min=1, max=5)])
    q16 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][16], default=1, validators=[NumberRange(min=1, max=5)])
    q17 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][17], default=1, validators=[NumberRange(min=1, max=5)])
    q18 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][18], default=1, validators=[NumberRange(min=1, max=5)])
    q19 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][19], default=1, validators=[NumberRange(min=1, max=5)])
    q20 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][20], default=1, validators=[NumberRange(min=1, max=5)])
    q21 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][21], default=1, validators=[NumberRange(min=1, max=5)])
    q22 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][22], default=1, validators=[NumberRange(min=1, max=5)])
    q23 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][23], default=1, validators=[NumberRange(min=1, max=5)])
    q24 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][24], default=1, validators=[NumberRange(min=1, max=5)])
    q25 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][25], default=1, validators=[NumberRange(min=1, max=5)])
    q26 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][26], default=1, validators=[NumberRange(min=1, max=5)])
    q27 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][27], default=1, validators=[NumberRange(min=1, max=5)])
    q28 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][28], default=1, validators=[NumberRange(min=1, max=5)])
    q29 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][29], default=1, validators=[NumberRange(min=1, max=5)])
    q30 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][30], default=1, validators=[NumberRange(min=1, max=5)])
    q31 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][31], default=1, validators=[NumberRange(min=1, max=5)])
    q32 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][32], default=1, validators=[NumberRange(min=1, max=5)])
    q33 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][33], default=1, validators=[NumberRange(min=1, max=5)])
    q34 = IntegerRangeField(label=names_and_ids.skill_names_and_ids['name'][34], default=1, validators=[NumberRange(min=1, max=5)])

    submit = SubmitField('Submit')

@app.route('/index/',  methods=['GET', 'POST'])
def index():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            q0 = form.q0.data
            q1 = form.q1.data
            q2 = form.q2.data
            q3 = form.q3.data
            q4 = form.q4.data
            q5 = form.q5.data
            q6 = form.q6.data
            q7 = form.q7.data
            q8 = form.q8.data
            q9 = form.q9.data
            q10 = form.q10.data
            q11 = form.q11.data
            q12 = form.q12.data
            q13 = form.q13.data
            q14 = form.q14.data
            q15 = form.q15.data
            q16 = form.q16.data
            q17 = form.q17.data
            q18 = form.q18.data
            q19 = form.q19.data
            q20 = form.q20.data
            q21 = form.q21.data
            q22 = form.q22.data
            q23 = form.q23.data
            q24 = form.q24.data
            q25 = form.q25.data
            q26 = form.q26.data
            q27 = form.q27.data
            q28 = form.q28.data
            q29 = form.q29.data
            q30 = form.q30.data
            q31 = form.q31.data
            q32 = form.q32.data
            q33 = form.q33.data
            q34 = form.q34.data

            prediction_data = [q0,q1,q2,q3,q4]
                               # q5, q6,q7,q8,q9,q10,
                               # q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,
                               # q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,
                               # q31,q32,q33,q34]

            _result = occupation_prediction.predict(prediction=prediction_data)
            result = _result.values

            vals = []
            for ind, row in _result.iterrows():
                val = {'cip':row[0] , 'prob':row[1], 'name_long':row[2]}
                vals.append(val)

            skills_data = []
            for ind, skill_pred in enumerate(prediction_data):
                skill = {'skill':names_and_ids.skill_names_and_ids['name'][ind],
                         'cip':names_and_ids.skill_names_and_ids['id'][ind],
                         'user_input':skill_pred}
                skills_data.append(skill)

            return render_template('results.html', result=result, vals=json.dumps(vals), skills_data=json.dumps(skills_data))

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.debug = True
    app.run()
