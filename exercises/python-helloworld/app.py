from flask import Flask,request
from logging import basicConfig,DEBUG
import time


basicConfig(filename="app.log",level=DEBUG)

app = Flask(__name__)

def log_endpoint(request: request):
    app.logger.info(f"{time.asctime()}, {request.path} endpoint was reached")
    

@app.route("/")
def hello():
    log_endpoint(request)
    return "Hello World!"

@app.route("/status")
def status():
    log_endpoint(request)
    return {"result": "OK - healthy"}

@app.route("/metrics")
def metrics():
    log_endpoint(request)
    return {"data": {"UserCount": 140, "UserCountActive": 23}}



if __name__ == "__main__":
    app.run(host='0.0.0.0')
