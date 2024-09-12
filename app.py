from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Predefined questions and answers in a DataFrame
df = pd.DataFrame({
    "question": ["What is the average lifespan of a dog?", "How often should I feed my dog?", "Can dogs see colors?", "How much exercise does a dog need?", "Can dogs hear better than humans?"],
    "answer": ["10-13 years", "2-3 times a day", "No, they are colorblind", "At least 30 minutes a day", "Yes, they can hear higher frequencies"]
})

# Chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.form["question"]
    answer = df.loc[df["question"].str.lower() == user_input.lower(), "answer"].values[0]
    return render_template("chatbot.html", question=user_input.capitalize(), answer=answer)

# Index route
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)