from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle blank input
    if text_to_analyze == "":
        return "Invalid input! Please try again."

    response = emotion_detector(text_to_analyze)

    # Handle invalid API response
    if response is None:
        return "Invalid input! Please try again."

    dominant_emotion = max(response, key=response.get)

    return (
        f"For the given statement, the system response is {response}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(debug=True)
