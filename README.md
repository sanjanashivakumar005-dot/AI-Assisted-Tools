# AI-Assisted-Tools
AI-Assisted tools for resttlement impact prediction
AI-Assisted Tools for Resettlement Impact Prediction
Project Description
This project demonstrates a simple AI-assisted toolset for predicting the impact of resettlement on households using machine learning techniques. It includes two main components:

Predictive Analysis Tool — Uses a dummy weighted linear model to estimate resettlement impact based on household features (e.g., demographics, location, income).

Fairness Analysis Tool — Evaluates fairness in model predictions across sensitive attributes, such as demographic groups, by comparing average predicted impacts.

This project provides insights into how predictive models can be analyzed for fairness and bias with respect to protected attributes, an essential aspect for ethical AI in resettlement and social impact assessments.

Features
Prediction of impact scores for individual households based on weighted features.

Group-wise fairness analysis by sensitive attributes, highlighting prediction disparities.

Flask-based web interface to visualize predictions and fairness reports dynamically.

Easy customization of household data and model parameters.

Technologies Used
Python 3: Core programming language.

Flask: Web framework used to build interactive browser interface.

Typing: For cleaner type annotations and data structure definitions.

Installation & Setup
Clone the repository or download project files.

Install Flask (if not already installed):

text
pip install flask
Run the Flask app:

text
python app.py
Open your browser and navigate to:

text
http://127.0.0.1:5000/
Usage
The default dataset includes example households with features and sensitive attribute values.

Modify household features or model weights in the Python code to test different scenarios.

View predictions and fairness summaries in the browser.

Extend the Flask app to input data dynamically if desired.

Future Work
Integrate real resettlement impact datasets.

Implement more sophisticated machine learning models.

Add detailed fairness metrics and mitigation techniques.

Enhance the web UI for better user interaction.



