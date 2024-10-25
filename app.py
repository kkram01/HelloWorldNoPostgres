"""Module providing a function printing hello world as a sample."""
# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from flask import Flask, request, jsonify
from apiflask import APIFlask, Schema
from apiflask.fields import String
from flask_swagger_ui import get_swaggerui_blueprint

app = APIFlask(__name__, title='HelloWorld API', version='1.0.0', spec_path='/openapi.json')
OPENAPI_URL = "/openapi"
API_URL = "/openapi.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    OPENAPI_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=OPENAPI_URL)

# openapi.info.description
app.config['DESCRIPTION'] = """
The description for this API. It can be very long and **Markdown** is supported.
"""

app.config['SERVERS'] = [
    {'name': 'Development Server', 'url': 'http://localhost:8080'}
]

class HelloWorldData(Schema):
    name = String()

@app.post("/")
@app.doc(summary='Sample Hello World method that says hello to your name', responses={"201" : "Successful"})
@app.input(HelloWorldData, location='json', example='{"name": "test-name"}')
def hello_world(json_data):
    """Sample Deployment Test."""
    name = json_data['name']
    return f"Hello! {name}", 201


@app.get("/healthcheck")
@app.doc(summary='Basic healthcheck that returns success', responses={"200" : "Successful"})
def health_check():
    """ health check """
    return "success", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
