pipeline {
    agent any

    stages {

        stage('Install') {
            steps {
                echo 'Installing dependencies...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t pratikragrawal/devops-app:v1 .'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push pratikragrawal/devops-app:v1'
            }
        }

        stage('Scan Image') {
            steps {
                bat 'trivy image pratikragrawal/devops-app:v1'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop my-app || exit 0'
                bat 'docker rm my-app || exit 0'
                bat 'docker run -d -p 3000:3000 --name my-app pratikragrawal/devops-app:v1'
            }
        }
    }
}