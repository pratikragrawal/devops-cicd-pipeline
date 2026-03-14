from flask import Flask, render_template, jsonify
from datetime import datetime
import logging
import os

# ----------------------------
# Application Configuration
# ----------------------------
class Config:
    APP_NAME = "DevOps CI/CD Pipeline"
    VERSION = "1.0"
    AUTHOR = ["Pratik Agrawal", "Aryan"]
    PORT = 5000


# ----------------------------
# Initialize Application
# ----------------------------
app = Flask(__name__)
app.config.from_object(Config)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def dashboard():
    logger.info("Dashboard accessed")
    return render_template(
        "index.html",
        project=app.config["APP_NAME"],
        version=app.config["VERSION"],
        time=datetime.now()
    )


@app.route("/api/health")
def health():
    logger.info("Health check requested")
    return jsonify({
        "status": "healthy",
        "service": app.config["APP_NAME"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/api/version")
def version():
    return jsonify({
        "application": app.config["APP_NAME"],
        "version": app.config["VERSION"],
        "authors": app.config["AUTHOR"]
    })


@app.route("/api/pipeline")
def pipeline():
    return jsonify({
        "pipeline": [
            "Developer Commit",
            "GitHub Repository",
            "Jenkins CI/CD Pipeline",
            "Docker Image Build",
            "Docker Hub Registry",
            "Kubernetes Deployment"
        ]
    })


# ----------------------------
# Error Handling
# ----------------------------

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


# ----------------------------
# Run Application
# ----------------------------

if __name__ == "__main__":
    logger.info("Starting DevOps CI/CD Application")
    app.run(host="0.0.0.0", port=app.config["PORT"])