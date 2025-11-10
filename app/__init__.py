from flask import Flask, jsonify, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/members')
    def members():
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        return jsonify(data)

    return app
