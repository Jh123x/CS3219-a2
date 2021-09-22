import math
from pprint import pprint
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calculations', methods=['GET', 'POST'])
def calculations():
    if request.method == "GET":
        return render_template('calculations.html')
    res = request.form
    if res is None:
        return render_template('calculations.html', input="Error")
    result = int(res.get('value'))
    return render_template(
        'calculations.html',
        input = result if res else "Error input",
        results = sorted(list(factorize(result))) if res else ["There is no result"]
    )

def factorize(number):
    """Factorize a number"""
    if number == 0:
        return ['Everything']
    factors = {1,}
    limit = int(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return factors

    


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)