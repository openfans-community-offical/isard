from flask import Flask

from engine.models.manager_hypervisors import ManagerHypervisors
from engine.services import db
from engine.services.lib.functions import check_tables_populated

app = Flask(__name__)
check_tables_populated()
app.m = ManagerHypervisors()
app.db = db

# register blueprints
from engine.api import api as api_blueprint

app.register_blueprint(api_blueprint, url_prefix='')  # url_prefix /api?
