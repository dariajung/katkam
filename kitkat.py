from flask import Flask
from flask import render_template
from CONFIG import IP_ADDRESS, CAT_PORT

app = Flask(__name__)

@app.route("/")
def hello(ip=IP_ADDRESS, port=CAT_PORT):
    print ip, port
    return render_template('kitkat.html', ip=ip, port=port)

if __name__ == "__main__":
    app.run()