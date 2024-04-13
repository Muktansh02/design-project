from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the pre-trained chatbot model from JSON
with open('models/healthhub1.json', 'r') as json_file:
    chatbot_model = json.load(json_file)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    # Process the user input and make predictions using the loaded model
    response = generate_response(message, cols)

    return jsonify({'response': response})


def generate_response(message, cols):
    # Convert the user input to the format expected by the model
    symptoms_present = [symptom in message.lower() for symptom in cols]

    # Use the model to make predictions
    prediction = clf.predict([symptoms_present])[0]

    # Get the predicted disease
    predicted_disease = le.inverse_transform([prediction])[0]

    # Get the symptoms associated with the predicted disease
    symptoms_associated = reduced_data.columns[reduced_data.loc[predicted_disease].values[0].nonzero()]

    # Format the prediction results as a response message
    response = f"Based on the symptoms you provided ({', '.join(symptoms_present)}), it seems you may have {predicted_disease}.\n"
    response += "Symptoms associated with this condition include: " + ', '.join(symptoms_associated) + "\n"

    # Call function to recommend doctors based on the predicted disease
    response += recommend_doctors(predicted_disease)

    # Generate graph based on symptoms provided by the user
    generate_graph(symptoms_present, predicted_disease)

    return response



if __name__ == '__main__':
    app.run(debug=True)
