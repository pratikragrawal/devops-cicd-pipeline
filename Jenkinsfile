pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/pratikragrawal/devops-cicd-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

    }
}