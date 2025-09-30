from flask import Flask, jsonify, render_template_string
import pandas as pd
import numpy as np

from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(
    "mysql+pymysql://",
    connect_args={
        "host": "172.16.16.33",
        "user": "hry",
        "password": "hry@8888",  # Password with @ goes here
        "database": "ry",
        "port": 3306,
        "charset": "utf8"
    }
)

# Serve front.html
@app.route("/")
def index():
    with open("front.html", encoding="utf-8") as f:
        html_content = f.read()
    return render_template_string(html_content)

# API endpoint to get SQL data
@app.route("/data")
def get_data():
    df = pd.read_sql("SELECT * FROM index_data", engine)
    df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
