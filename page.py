from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route("/")
def test():
    return render_template('entry_form.html')

if __name__ == '__main__':
    app.run(debug=True)