import logging
from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, FrontEnd info logs", version="1.0.0")

@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/healthz')
def healthcheck():
    return jsonify({"result":"OK - healthy"})


if __name__ == "__main__":
    app.run(debug=False)