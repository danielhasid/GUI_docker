pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
        }
    }

    stages {
        stage('Setup') {
            steps {
                // Verify current user is root
                sh 'whoami'

                // Fix directory permissions just in case
                sh 'mkdir -p /var/lib/apt/lists/partial && chmod -R 755 /var/lib/apt/lists'

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
     
