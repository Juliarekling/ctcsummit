from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speakers')
def speakers():
    return render_template('speakers.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
