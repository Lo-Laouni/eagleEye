from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/info')
def devInfo():
    return render_template('devInfo.html')


@app.route('/data')
def devData():
    return render_template('devData.html')


@app.route('/operations')
def devOp():
    return render_template('devOp.html')


@app.route('/configs')
def devConfig():
    return render_template('devConfig.html')


@app.route('/')
def logout():
    return render_template('logout.html')

if __name__ == "__main__":
    app.run(debug=True)