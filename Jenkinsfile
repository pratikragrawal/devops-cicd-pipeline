pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/pratikragrawal/devops-cicd-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python --version'
            }
        }

        stage('Push Docker Image') {
    steps {
        bat 'docker push pratikragrawal/devops-app:v1'
    }
}