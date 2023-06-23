# javascript tip:
# to edit the html or webpage freely, right click and click the inspect
# and go to console and type document.body.contentEditable=true
# document.body.contentEditable=true

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
