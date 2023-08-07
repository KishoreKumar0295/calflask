from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(num1, num2)
            operator = "+"
        elif operation == "subtract":
            result = subtract(num1, num2)
            operator = "-"
        elif operation == "multiply":
            result = multiply(num1, num2)
            operator = "*"
        elif operation == "divide":
            try:
                result = divide(num1, num2)
                operator = "/"
            except ValueError as e:
                return render_template("index.html", error=str(e))

        return render_template("index.html", result=result, operator=operator)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
