pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rahulroli/second_devops_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t devops-test-app:latest .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if running
                    sh 'docker rm -f devops-test-app || true'
                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name devops-test-app devops-test-app:latest'
                }
            }
        }
    }
}
