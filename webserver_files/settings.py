from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)


def load_config():
    config_file = open(
        "/Users/riobeggs/Documents/code/web_server/webserver_files/config.json"
    )
    data = json.load(config_file)
    return data


def get_url(user: str, password: str, host: str, port: int, dbname: str) -> str:
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return url


json = load_config()

user = json["user"]
password = json["password"]
host = json["host"]
port = json["port"]
dbname = json["dbname"]

url = get_url(user, password, host, port, dbname)
app.config["SQLALCHEMY_DATABASE_URI"] = url
database = SQLAlchemy(app)  # L4
db = database
