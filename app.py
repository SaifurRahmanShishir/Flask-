from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

app = Flask(__name__)



# Create an initial empty model
model = LinearRegression()

# Sample data (replace with your own dataset)


df = pd.read_csv('data\\readmission_demo.csv')[['Chronic_cond', 'sdoh_Transportation_barrier', 'PROGRAMS_CONTRIB']].dropna().reset_index(drop = True)


X = df[['Chronic_cond', 'sdoh_Transportation_barrier']]
Y = df['PROGRAMS_CONTRIB']

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size = 0.8) 

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        if request.form.get('train_model'):
            try:
                # Fit the model with the training data
                model.fit(X_train, y_train)
                mse = mean_squared_error(y_true = y_test, y_pred = model.predict(X_test))
                return jsonify({'message': 'Model trained successfully!', 'Modelperformance': f'The MSE = {mse}'})
            except Exception as e:
                return jsonify({'error': str(e)})
        elif request.form.get('predict'):
            try:
                # Get user-provided feature from the form
                # Get user-provided feature values from the form
                feature1 = float(request.form['feature1'])
                feature2 = float(request.form['feature2'])

                # Make a prediction using the trained model
                prediction = model.predict(np.array([[feature1, feature2]]))
                return jsonify({'prediction': prediction[0]})      
            except Exception as e:
                return jsonify({'error': str(e)})
    return render_template('index.html', prediction=prediction)


@app.route('/ID', methods = ['GET'])
def seccond():

    params_value = request.args.get('id')
    
    if params_value == '1':
        return jsonify('The name is Silva')
    
    else:
        return jsonify('Please enter the correct ID')







if __name__ == '__main__':
    app.run(debug = True)
