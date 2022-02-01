from flask import Flask, render_template
from article import Articles

main = Flask (__name__)

Bulletin = Bulletin ()

@main.route('/')
def index():
    return render_template('main.html')

@main.route('/about')
def about():
    return render_template ('about.html')

@main.route('/bulletin')
def bulletin():
    return render_template ('bulletin.html', articles =Articles)

if __name__ == '__main__':
    main.run (debug=True)


