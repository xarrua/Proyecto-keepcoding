from flask import Flask


app = Flask(__name__,instance_relative_config=True)

app.config.from_object("config")

ORIGIN_DATA="data/registros.sqlite"


from registros_med.routes import *

