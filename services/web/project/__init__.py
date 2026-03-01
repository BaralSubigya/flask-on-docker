import os
from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # DB config
    from .config import Config
    app.config.from_object(Config)
    db.init_app(app)

    # Media folder config
    base_dir = os.path.dirname(os.path.abspath(__file__))
    media_folder = os.path.join(base_dir, "media")
    os.makedirs(media_folder, exist_ok=True)
    app.config["MEDIA_FOLDER"] = media_folder

    # Import models so SQLAlchemy knows them
    from .models import User  # noqa: F401

    @app.route("/")
    def hello_world():
        return jsonify(hello="world")

    @app.route("/upload", methods=["POST"])
    def upload_file():
        if "file" not in request.files:
            return jsonify(error="No file field named 'file'"), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify(error="Empty filename"), 400

        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config["MEDIA_FOLDER"], filename)
        file.save(save_path)

        return jsonify(
            uploaded=filename,
            url=f"/media/{filename}"
        )

    @app.route("/media/<path:filename>")
    def media(filename):
        return send_from_directory(app.config["MEDIA_FOLDER"], filename)

    return app
