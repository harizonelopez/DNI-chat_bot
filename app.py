from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
app.secret_key = 'aladinh-montext'

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm doing well, thank you!", "I'm great. How about you?"]],
    ["what is your name", ["I'm a chatbot.", "You can call me ChatGPT."]],
    ["quit", ["Goodbye!", "Bye!", "Nice chatting with you."]],
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    error_message = "Oops!! The text seems not to be found."
    user_input = request.form["user_input"]
    
    if user_input.lower() == 'quit':
        response = "Goodbye!"
    else:
        response = chatbot.respond(user_input)

    return render_template("home.html", user_input=user_input, response=response, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
