pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git url: 'https://github.com/danielhasid/GUI_docker.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Build the application, e.g., installing dependencies
                sh 'pip install -r reqs.txt'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest
                sh 'pytest -v -s'
            }
        }

        stage('Deploy') {
            steps {
                // Deployment steps go here, e.g., copying files, running scripts, etc.
                echo 'Deploying application...'
                // Example deployment command (modify based on your deployment needs)
                // sh 'scp -r . user@remote_server:/path/to/deploy'
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
