import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


@app.route("/")
def index():
       print ("<h1>Hello World in Flask and Welcome</h1>")
