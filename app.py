from flask import Flask, request, render_template
import os

from src.pipeline.predict_pipeline import Predict_pipeline, CustomData

application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', form_data={})

    form_data = request.form.to_dict()
    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score')),
        )
        prediction = Predict_pipeline().predict(data.get_data_as_data_frame())
        return render_template(
            'home.html',
            result=round(float(prediction[0]), 1),
            form_data=form_data,
        )
    except (TypeError, ValueError):
        return render_template(
            'home.html',
            error='Please complete every field with a valid score between 0 and 100.',
            form_data=form_data,
        ), 400
    except Exception:
        app.logger.exception('Prediction failed')
        return render_template(
            'home.html',
            error='We could not generate a prediction right now. Please try again shortly.',
            form_data=form_data,
        ), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
