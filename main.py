from flask import Flask, render_template

main = Flask (__name__)

@main.route('/')
def index():
    return render_template('main.html')

@main.route('/')
def about():
    return render_template ('about.html')

if __name__ == '__main__':
    main.run (debug=True)


