pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root' // Run the container as root
        }
    }

    stages {
        stage('Setup') {
            steps {
                // Install Python and pip with root privileges
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
                sh 'pip install -r reqs.txt'
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
