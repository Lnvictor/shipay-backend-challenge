import json

from flask import Flask, jsonify, request

from .base import Session
from .controller import create_user, get_user_info
from .models import User

app = Flask(__name__)


@app.route("/user/<int:id>", methods=["GET"])
def index(id):
    data = get_user_info(Session, id)
    resp = [
        {
            "name": row[0].name,
            "email": row[0].email,
            "claim_description": row[1],
            "role_description": row[2],
        }
        for row in data
    ]
    return jsonify(resp)


@app.route("/user", methods=["POST"])
def create():
    data = json.loads(request.data)
    create_user(Session, data)
    return jsonify({"message": "created"}), 201
