pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-app"
        DOCKERHUB_USER = "pratikragrawal"
        IMAGE_TAG = "v1"
        DOCKER_PASSWORD = "Pratik@2005"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/pratikragrawal/devops-cicd-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag %IMAGE_NAME%:%IMAGE_TAG% %DOCKERHUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Docker Login') {
            steps {
                bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKERHUB_USER% --password-stdin'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker push %DOCKERHUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                bat 'trivy image %DOCKERHUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Deploy to Kubernetes') {
    steps {
        echo 'Deployment will be done manually using kubectl'
    }
}
}

    post {
        success {
            echo 'Pipeline executed successfully 🚀'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}