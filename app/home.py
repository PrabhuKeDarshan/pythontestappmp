from flask import Flask, render_template

#def _name_ = '0'

app = Flask(__name__)


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/story1/')
def story1():
    return render_template('story1.html')


if __name__ == "__main__":
    app.run(debug = True)
