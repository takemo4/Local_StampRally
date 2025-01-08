from flask import Blueprint, jsonify
from backend.models import db,StampRally, Spot, StampStatus

# ルートの登録
def register_routes(app):
    @app.route('/')
    def index():
        return "Welcome to the Stamp Rally API!"