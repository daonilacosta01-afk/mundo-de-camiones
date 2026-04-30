from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motor')
def motor():
    return render_template('motor.html')

@app.route('/transmision')
def transmision():
    return render_template('transmision.html')

@app.route('/diferencial')
def diferencial():
    return render_template('diferencial.html')

@app.route('/carroceria')
def carroceria():
    return render_template('carroceria.html')

@app.route('/gomas')
def gomas():
    return render_template('gomas.html')

if __name__ == '__main__':
    app.run(debug=True)