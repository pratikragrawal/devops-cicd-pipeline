from flask import Flask
import subprocess
import webbrowser
import platform

app = Flask(__name__)

# ---------- HELPER ----------
def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode()
    except:
        return "Service not available"

# ---------- HOME (PROFESSIONAL UI) ----------
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Devops Application</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f172a, #020617);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                text-align: center;
                padding: 40px;
                border-radius: 15px;
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(10px);
                box-shadow: 0 0 20px rgba(0,255,255,0.2);
                width: 400px;
            }

            h1 {
                font-size: 28px;
                margin-bottom: 10px;
            }

            p {
                opacity: 0.7;
                margin-bottom: 20px;
            }

            .btn {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }

            .primary {
                background: #22c55e;
                color: black;
            }

            .secondary {
                background: #1e293b;
                color: white;
            }

            .btn:hover {
                transform: scale(1.05);
            }

            .status {
                margin-top: 20px;
                padding: 8px 15px;
                border-radius: 20px;
                display: inline-block;
                background: #22c55e;
                color: black;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h1>🚀 Devops demo Application</h1>
            <p>CI/CD Pipeline using Docker, Kubernetes & Trivy</p>

            <a href="/dashboard" class="btn primary">View Dashboard</a>
            <a href="/health" class="btn secondary">Health Check</a>

            <div class="status">Application Running</div>
        </div>

    </body>
    </html>
    """

# ---------- HEALTH ----------
@app.route('/health')
def health():
    return {"status": "healthy"}

# ---------- DASHBOARD ----------
@app.route('/dashboard')
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Devops Monitoring Dashboard</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #020617, #0f172a);
                color: white;
            }

            h1 {
                text-align: center;
                padding: 20px;
            }

            .section {
                margin: 30px;
            }

            .section h2 {
                opacity: 0.8;
            }

            .grid {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
            }

            .card {
                width: 200px;
                padding: 20px;
                border-radius: 12px;
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(10px);
                box-shadow: 0 0 15px rgba(0,255,255,0.2);
                text-align: center;
                cursor: pointer;
                transition: 0.3s;
            }

            .card:hover {
                transform: scale(1.05);
                box-shadow: 0 0 25px rgba(0,255,255,0.6);
            }

            .status {
                margin-top: 10px;
                padding: 5px 10px;
                border-radius: 15px;
                background: #22c55e;
                color: black;
                font-weight: bold;
                font-size: 13px;
            }

            .pipeline {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 20px;
            }

            .step {
                padding: 10px 15px;
                background: #1e293b;
                border-radius: 8px;
            }

            .arrow {
                font-size: 18px;
                color: #22c55e;
            }
        </style>
    </head>

    <body>

    <h1>🚀 DevSecOps CI/CD Dashboard</h1>

    <div class="section">
        <h2>🔄 Pipeline Flow</h2>
        <div class="pipeline">
            <div class="step">GitHub</div>
            <div class="arrow">→</div>
            <div class="step">Jenkins</div>
            <div class="arrow">→</div>
            <div class="step">Testing</div>
            <div class="arrow">→</div>
            <div class="step">Docker</div>
            <div class="arrow">→</div>
            <div class="step">Docker Hub</div>
            <div class="arrow">→</div>
            <div class="step">Trivy</div>
            <div class="arrow">→</div>
            <div class="step">Kubernetes</div>
        </div>
    </div>

    <div class="section">
        <h2>🔧 Services</h2>
        <div class="grid">

            <div class="card" onclick="window.open('http://localhost:8080')">
                Jenkins
                <div class="status">RUNNING</div>
            </div>

            <div class="card" onclick="window.open('/docker')">
                Docker
                <div class="status">ACTIVE</div>
            </div>

            <div class="card" onclick="window.open('/pods')">
                Kubernetes
                <div class="status">DEPLOYED</div>
            </div>

            <div class="card" onclick="window.open('https://hub.docker.com/r/pratikragrawal/devops-app')">
                Docker Hub
                <div class="status">AVAILABLE</div>
            </div>

            <div class="card" onclick="window.open('/open-app')">
                Application
                <div class="status">LIVE</div>
            </div>

        </div>
    </div>

    <div class="section">
        <h2>📊 Monitoring</h2>
        <div class="grid">

            <div class="card" onclick="window.open('/pods')">
                Pod Status
                <div class="status">CHECK</div>
            </div>

            <div class="card" onclick="window.open('/docker')">
                Containers
                <div class="status">CHECK</div>
            </div>

            <div class="card" onclick="window.open('/system')">
                System Info
                <div class="status">VIEW</div>
            </div>

        </div>
    </div>

    </body>
    </html>
    """

# ---------- STATUS ----------
@app.route('/pods')
def pods():
    return f"<pre>{run_command('kubectl get pods')}</pre>"

@app.route('/docker')
def docker():
    return f"<pre>{run_command('docker ps')}</pre>"

@app.route('/system')
def system():
    return f"""
    <pre>
OS: {platform.system()}
Node: {platform.node()}
Processor: {platform.processor()}
    </pre>
    """

@app.route('/open-app')
def open_app():
    webbrowser.open("http://localhost:5000")
    return "<h2>Application ✅</h2>"

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)