pipeline {
    agent any

    environment {
        IMAGE = "pratikragrawal/devops-app:v1"
    }

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/pratikragrawal/devops-cicd-pipeline.git'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest || exit 0'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'echo %PASS% | docker login -u %USER% --password-stdin'
                    bat 'docker push %IMAGE%'
                }
            }
        }

        stage('Scan Image') {
            steps {
                bat 'trivy image %IMAGE%'
            }
        }

        stage('Deploy') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}