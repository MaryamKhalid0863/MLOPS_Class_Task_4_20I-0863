from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
