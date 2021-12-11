from flask import Flask , redirect , url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'WELCOME tO mY FAVORITE WebSite!  :  https://www.wikipedia.org/   -   https://www.ed.ted.com/'

@app.route('/aboutme')
def about_func():
    return " welcome to about1 page"


@app.route('/contact')
def catalog1_func():
    return redirect(url_for('about_func'))


if __name__ == '__main__':
    app.run(debug=True)
