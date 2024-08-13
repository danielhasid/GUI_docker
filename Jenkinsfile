pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Install necessary system packages with root privileges
                sh '''
                    apt-get update && \
                    apt-get install -y python3 python3-pip wget unzip && \
                    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
                    apt install -y ./google-chrome-stable_current_amd64.deb && \
                    rm google-chrome-stable_current_amd64.deb && \
                    apt-get clean
                '''
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
