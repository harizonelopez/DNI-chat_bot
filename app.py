from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
app.secret_key = 'aladinh-montext'

pairs = [
    ["hi|hello|hey|hy", ["Hello!", "Hi there!", "Hey!", "Hello, how can I assist you today!"]],
    ["how are you|how are you today|how are you doing", ["I'm doing well, thank you!", "I'm great. How about you?", "I'm cool, so what's up?"]],
    ["what is your name", ["I'm a D.N.I chatbot.", "You can simply call me DNI as your wish."]],
    ["quit|q|close", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool, it was nice interacting with you."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means your DIGNITY NATURES YOUR IDENTITY.", "DIGNITY NATURES YOUR IDENTITY", "This is the abbreviation of DIGNITY NATURES YOUR IDENTITY"]],
    ["which programming language were you developed of|which programming language was used in  your development", ["I was made using pythoon language", "basically its python-flask framework", "the base language is python"]],
    ["who is your developer|who developed you|who is your co-founder|who created you|who created DNI|who created D.N.I chatbot", ["I'm was developed by Harison.O.O", "My co-founder is Harison.O.O", "That's a nice question, I was developed by developer Harison.O.O", "I was developed by developer Harison.O.O"]],
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
