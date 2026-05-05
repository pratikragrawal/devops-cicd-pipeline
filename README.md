\# DevOps CI/CD Pipeline using Docker and Kubernetes



\## Project Overview

This project demonstrates the implementation of an automated DevOps CI/CD pipeline using GitHub, Jenkins, Docker, and Kubernetes.



The pipeline automates the process of building, containerizing, and deploying an application.



\## Technologies Used

\- GitHub (Version Control)

\- Jenkins (CI/CD Automation)

\- Docker (Containerization)

\- Docker Hub (Container Registry)

\- Kubernetes / Minikube (Container Orchestration)

\- Python Flask (Web Application)



\## CI/CD Workflow

Developer pushes code to GitHub  

↓  

Jenkins pipeline triggers automatically  

↓  

Docker image is built  

↓  

Image is pushed to Docker Hub  

↓  

Kubernetes deploys the containerized application  



\## Project Structure

devops-cicd-pipeline

│

├── app.py

├── Dockerfile

├── Jenkinsfile

├── requirements.txt

├── deployment.yaml

└── service.yaml



\## Authors

Pratik Agrawal  

Aryan

