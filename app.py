from flask import Flask, render_template_string
from typing import List, Dict

app = Flask(__name__)


# Define the Household class
class Household:
    def __init__(self, id: int, features: List[float], ground_truth_impact: float):
        self.id = id
        self.features = features  # e.g., demographics, location data, income, etc.
        self.ground_truth_impact = ground_truth_impact  # for validation


# Predictive Analysis Tool (Dummy ML Model)
class PredictiveAnalysisTool:
    def __init__(self, model_weights: List[float] = None):
        self.model_weights = model_weights if model_weights is not None else [0.4, 0.3, 0.3]

    def predict(self, features: List[float]) -> float:
        score = 0.0
        for i in range(min(len(self.model_weights), len(features))):
            score += self.model_weights[i] * features[i]
        return score

    def predict_all(self, households: List[Household]) -> List[Dict]:
        return [
            {"id": hh.id, "predicted_impact": self.predict(hh.features)}
            for hh in households
        ]


# Fairness Analysis Tool
class FairnessAnalysisTool:
    def __init__(self, sensitive_feature_index: int):
        self.sensitive_feature_index = sensitive_feature_index

    def group_by_sensitive_attribute(self, households: List[Household]) -> Dict:
        groups = {}
        for hh in households:
            key = hh.features[self.sensitive_feature_index]
            groups.setdefault(key, []).append(hh)
        return groups

    def analyze_fairness(self, households: List[Household], predictive_tool: PredictiveAnalysisTool) -> Dict:
        groups = self.group_by_sensitive_attribute(households)
        group_stats = {}
        for key, group in groups.items():
            preds = [predictive_tool.predict(hh.features) for hh in group]
            avg_pred = sum(preds) / len(preds) if preds else 0.0
            group_stats[key] = {"avg_pred_impact": avg_pred, "count": len(preds)}
        return group_stats


# Example data
example_households = [
    Household(1, [0, 0.8, 0.3], 0.7),
    Household(2, [1, 0.5, 0.5], 0.5),
    Household(3, [0, 0.7, 0.6], 0.8),
    Household(4, [1, 0.4, 0.2], 0.4)
]


@app.route('/')
def index():
    predictive_tool = PredictiveAnalysisTool()
    predictions = predictive_tool.predict_all(example_households)

    fairness_tool = FairnessAnalysisTool(0)  # sensitive attribute at index 0
    fairness_report = fairness_tool.analyze_fairness(example_households, predictive_tool)

    html_template = """
    <html>
    <head><title>Resettlement Impact Prediction</title></head>
    <body>
        <h2>Predictions</h2>
        <table border="1" cellpadding="5">
            <tr><th>ID</th><th>Predicted Impact</th></tr>
            {% for p in predictions %}
            <tr><td>{{p['id']}}</td><td>{{'%.2f' % p['predicted_impact']}}</td></tr>
            {% endfor %}
        </table>

        <h2>Fairness Report by Sensitive Attribute</h2>
        <table border="1" cellpadding="5">
            <tr><th>Group</th><th>Average Predicted Impact</th><th>Count</th></tr>
            {% for key, val in fairness_report.items() %}
            <tr>
                <td>{{key}}</td>
                <td>{{'%.2f' % val['avg_pred_impact']}}</td>
                <td>{{val['count']}}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html_template, predictions=predictions, fairness_report=fairness_report)


if __name__ == '__main__':
    app.run(debug=True)
