from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

engine = pyttsx3.init()

@app.route("/")
def index():
    return """
    <h1>AI Avatar Studio</h1>
    <form method="post">
        <input name="text" placeholder="Введите текст">
        <button type="submit">Говорить</button>
    </form>
    """

@app.route("/", methods=["POST"])
def speak():
    text = request.form["text"]
    engine.say(text)
    engine.runAndWait()
    return "Готово"

if __name__ == "__main__":
    app.run(debug=True)
