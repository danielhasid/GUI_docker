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
                // Checkout code from the GitHub repository
                echo 'Checkout'
            }
        }

        stage('Build') {
            steps {
                  echo 'build'

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
