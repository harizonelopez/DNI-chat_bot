from flask import Flask, render_template, request, redirect, url_for
from nltk.chat.util import Chat, reflections
import random
import logging

app = Flask(__name__)
app.config['SECRET_KEY']='aladinh00-010montext'
logging.basicConfig(level=logging.DEBUG)

pairs = [
    ["who is harison.o.o|harison is who|who is harison", ["this name refers to my creator and developer, a computer science student at one of the main universities in kenya", "harison is a tech student at murang'a university in kenya", "harison is a coding enthusiast who came up with the idea to develop a chatbot called D.N.I."]],
    ["hi|hello|hey|hy|yoh what's up|hey niggah|hey buddy", ["hello!", "hi there!", "hey!", "hello, how can I assist you today!"]],
    ["how are you|how are you today|how are you doing", ["I'm doing well, thank you!", "I'm great. how about you?", "I'm cool, so what's up?"]],
    ["okay|cool|thanks|thank you|your welcome|ok", ["Your welcome, how can I help you today", "That's awesome", "I appreciate, I hope you are cool also"]],
    ["what is your name|what is your identity|how do i call you", ["You can simply call me DNI as your wish.", "I'm D.N.I chatbot."]],
    ["which services do you provide|what are the things you offer|services you offer|things you offer|what do you do", ["I mainly offer services related to technology", "My main focus is to provide you with tech related things", "I can offer you with variety of things mainly dwelling around tech."]],
    ["quit|q|close", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool, it was nice interacting with you."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means your DIGNITY NATURES YOUR IDENTITY.", "DIGNITY NATURES YOUR IDENTITY", "This is the abbreviation of DIGNITY NATURES YOUR IDENTITY"]],
    ["which programming language were you developed of|which programming language was used in  your development", ["I was made using pythoon language", "basically its python-flask framework", "the base language is python"]],
    ["who is your developer|who developed you|who is your co-founder|who created you|who created DNI|who created D.N.I chatbot", ["I'm was developed by harison.o.o", "My co-founder is harison.o.o", "That's a nice question, I was developed by developer harison.o.o", "I was developed by developer harison.o.o"]],
]

chatbot = Chat(pairs, reflections)
chat_history=[]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    error_message = "404 ERROR, response is not validated."
    user_input = request.form["user_input"].lower()
    response = None
    for pair in pairs:
        keywords = pair[0].lower().split('|')
        for keyword in keywords:
            if keyword in user_input:
                response = random.choice(pair[1])
                return render_template("home.html", user_input=user_input, response=response, error_message=error_message)
    
    response = chatbot.respond(user_input)
    chat_history.append({"user_input": user_input, "response": response})
    print(f"Chat history:", chat_history)
    
    return render_template("home.html", user_input=user_input, response=response, error_message=error_message, chat_history=chat_history)

@app.route("/history")
def history():    
    return render_template("index.html", chat_history=chat_history)

@app.route("/clear_history", methods=["POST"])
def clear_history():
    global chat_history
    chat_history = []
    return redirect(url_for("history"))

if __name__ == "__main__":
    app.run(debug=True)
