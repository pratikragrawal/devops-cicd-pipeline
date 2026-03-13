from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>DevOps CI/CD Dashboard</title>

<style>
body {
    font-family: Arial;
    background: linear-gradient(135deg,#1f4037,#99f2c8);
    margin:0;
}

.container{
    width:80%;
    margin:auto;
    text-align:center;
    padding:40px;
}

.card{
    background:white;
    padding:25px;
    border-radius:10px;
    box-shadow:0 4px 10px rgba(0,0,0,0.2);
    margin-top:20px;
}

h1{
    color:#2c3e50;
}

.status{
    color:green;
    font-weight:bold;
}

.step{
    display:inline-block;
    background:#3498db;
    color:white;
    padding:10px 15px;
    margin:5px;
    border-radius:5px;
}
</style>

</head>

<body>

<div class="container">

<h1>🚀 DevOps CI/CD Pipeline Dashboard</h1>

<div class="card">
<h2>Project Information</h2>
<p><b>Project:</b> Automated CI/CD Pipeline</p>
<p><b>Technologies:</b> GitHub • Jenkins • Docker • Kubernetes</p>
<p><b>Status:</b> <span class="status">Application Running Successfully</span></p>
<p><b>Server Time:</b> {{time}}</p>
</div>

<div class="card">
<h2>CI/CD Workflow</h2>

<span class="step">Developer</span>
<span class="step">GitHub</span>
<span class="step">Jenkins</span>
<span class="step">Docker</span>
<span class="step">Docker Hub</span>
<span class="step">Kubernetes</span>

</div>

<div class="card">
<h2>Team Members</h2>
<p>Pratik Agrawal</p>
<p>Aryan</p>
</div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, time=datetime.now())

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/version")
def version():
    return {"version": "1.0", "project": "DevOps CI/CD Pipeline"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)