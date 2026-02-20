from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temp = request.form.get('temperature')
        unit = request.form.get('unit')

        try:
            temp = float(temp)
            if unit == 'C':
                result = f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F | {celsius_to_kelvin(temp):.2f}K"
            elif unit == 'F':
                c = fahrenheit_to_celsius(temp)
                result = f"{temp}°F = {c:.2f}°C | {celsius_to_kelvin(c):.2f}K"
            elif unit == 'K':
                c = kelvin_to_celsius(temp)
                result = f"{temp}K = {c:.2f}°C | {celsius_to_fahrenheit(c):.2f}°F"
        except ValueError:
            result = "Please enter a valid number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
