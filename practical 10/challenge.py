from flask import Flask, request

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    except ValueError:
        return "Invalid input. Please enter a numeric value for Celsius."


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{celsius}°C is equal to {fahrenheit}°F"


app.run()
