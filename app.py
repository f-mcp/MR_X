"""
FLASK TRIAL
"""


from flask import Flask, render_template, request
from questions import question_store



app = Flask(__name__)


@app.route('/')
def home():
    condition = True  # Change this to True/False to test rendering
    return render_template('Home.html', condition=condition)  # The main page with your HTML

@app.route('/instructions')
def instructions():
    print("bum")
    return render_template('Instructions.html')  # Create this HTML file

@app.route('/clues', methods=['GET', 'POST'])
def clues():
    if request.method == 'POST':
        question_index = request.form['question_index']
        user_answer = request.form['answer']

        # Update the state based on the user's answer
        if question_index in question_store:
            question_data = question_store[question_index]
            correct_answer = question_data[1]

            if user_answer.strip().lower() == correct_answer.lower():
                question_data[3] = 2  # Mark as completed
            else:
                question_data[3] = 1  # Mark as attempted



    return render_template('Clue.html', question_store=question_store)

@app.route('/hints')
def hints():
    return render_template('Hints.html')  # Create this HTML file

@app.route('/submit', methods=['POST'])
def submit_answer():



    name = request.form['name']
    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run(debug=True)
