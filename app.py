from flask import Flask, render_template, redirect, url_for, request
from random import randint, choice


app = Flask(__name__)


OPERATORS = {
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
}
EASY = [-2, -1, 0, 1, 2]
previous_operators = ['/', '*']


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def random_equation():
    global previous_operators
    while True:
        while True:
            operator = choice(list(OPERATORS.keys()))
            if operator not in previous_operators:
                previous_operators.append(operator)
                if len(previous_operators) > 2:
                    previous_operators.pop(0)
                break
        print(previous_operators)
        if operator in ['+', '-']:
            number_a = randint(1, 100)
            number_b = randint(1, 100)
        elif operator in ['*', '/']:
            number_a = randint(1, 20)
            number_b = randint(1, 20)
        correct = OPERATORS[operator](number_a, number_b)
        if is_integer_num(correct) and number_a != number_b:
            if correct not in EASY and number_a not in EASY and number_b not in EASY:
                return int(number_a), int(number_b), operator, int(correct)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    global score
    if request.method == "POST":
        correct = request.form["correct"]
        answer = request.form["answer"]
        if answer == correct:
            score += 1
        else:
            score -= 2
    number_a, number_b, operator, correct = random_equation()
    return render_template("index.html", number_a=number_a, number_b=number_b, operator=operator, correct=correct, score=score)


if __name__ == "__main__":
    score = 0
    app.run(debug=True)