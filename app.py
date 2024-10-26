from flask import Flask, render_template, request
import random
from run_model import get_predictions
from run_model2 import get_work_conditions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def Hello():
    context = ""

    # get the data from the form
    if request.method == 'POST':
        temp1 = request.form['temperature1']
        temp2 = request.form['temperature2']
        light1 = request.form['light1']
        light2 = request.form['light2']

        context = get_predictions(temp1, temp2,light1, light2)

    # send the data to a value
    return render_template('index.html', context=context)


@app.route('/WorkConditions', methods=['GET', 'POST'])

def work_conditions():
    context = ""
    temps = ""
    lights = ""

    # retrieve data from form 
    if request.method == 'POST':
        writing_speed1 = request.form['productivity1']
        writing_speed2 = request.form['productivity2']
        writing_speed3 = request.form['productivity3']

        results = get_work_conditions(writing_speed1, writing_speed2, writing_speed3)
        
        temps = results[0][:3]
        lights = results[0][3:]


    return render_template("conditions.html", temps=temps, lights=lights)

if __name__ == '__main__':
    app.run(debug=True)