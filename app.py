from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/field')
def field():
    return render_template('field.html')


if __name__ == '__main__':
    app.run()
