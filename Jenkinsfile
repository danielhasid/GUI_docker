pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Install Python and pip (for Debian/Ubuntu-based systems)
                sh 'apt-get update && apt-get install -y python3 python3-pip'
            }
        }

        stage('Checkout') {
            steps {
                git url: 'https://github.com/danielhasid/GUI_docker.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Use Python3 and pip3
                sh 'pip3 install -r reqs.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
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
