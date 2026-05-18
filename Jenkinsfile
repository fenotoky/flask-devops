pipeline {

    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/fenotoky/flask-devops.git'
            }
        }

        stage('Python Tests') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t localhost:4000/flask_hello .'
            }
        }

        stage('Docker Push') {
            steps {
                bat 'docker push localhost:4000/flask_hello'
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}