import logging

import pymongo
from flask import Flask, jsonify, render_template, request
from flask_opentracing import FlaskTracing
from flask_pymongo import PyMongo
from jaeger_client import Config
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, BackEnd info logs", version="1.0.0")

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)


config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1
        },
        'logging': True,
        'reporter_batch_size': 1,
    },
    service_name="backend-service"
)

jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)

@app.route('/')
def homepage():
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

@app.route('/healthz')
def healthcheck():
    return jsonify({"result":"OK - healthy"})


if __name__ == "__main__":
    app.run(debug=False)
