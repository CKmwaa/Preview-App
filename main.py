from flask import Flask, render_template
from bulletin import Bulletin

main = Flask (__name__)

Bulletin = Bulletin()

@main.route('/')
def index():
    return render_template('main.html')

@main.route('/about')
def about():
    return render_template ('about.html')

@main.route('/bulletin')
def bulletin():
    return render_template ('bulletin.html', bulletin = Bulletin)

@main.route('/bulletins/<string:id>/')
def bulletins(id):
    return render_template ('bulletins.html', id=id)


if __name__ == '__main__':

    main.run(debug=True)


