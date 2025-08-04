from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data(table):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speakers")
def speakers():
    speakers_data = get_data('speakers')
    return render_template("speakers.html", speakers=speakers_data)

@app.route("/partners")
def partners():
    partners_data = get_data('partners')
    return render_template("partners.html", partners=partners_data)

if __name__ == "__main__":
    app.run(debug=True)
