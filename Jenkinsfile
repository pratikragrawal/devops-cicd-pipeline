pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask'
            }
        }

        stage('Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Verify Application File') {
            steps {
                bat 'dir'
            }
        }

    }
}