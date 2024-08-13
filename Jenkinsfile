pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                echo 'setup'
            }
        }

        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'frontend', url: 'https://github.com/danielhasid/GUI_docker.git']])
            }
        }

        stage('Build') {
            steps {
                  docker build -t frontend .

            }
        }

        stage('Test') {
            steps {
                // Run tests
                echo 'test'

            }
        }

        stage('Deploy') {
            steps {
                // Deployment steps (customize as needed)
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
