from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def hello(ip=os.environ['KATKAM_IP_ADDRESS'], port=os.environ['KATKAM_PORT']):
    return render_template('kitkat.html', ip=ip, port=port)

if __name__ == "__main__":
    app.run()