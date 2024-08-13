pipeline {
    agent {
            docker {
                image 'ubuntu:22.04'
                args '-u root'
            }
        }
    stages {
        stage('Setup') {
            steps steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip wget unzip'
                sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
                sh 'apt install -y ./google-chrome-stable_current_amd64.deb'
                sh 'rm google-chrome-stable_current_amd64.deb'
                sh 'apt-get clean'
            }
        }

        stage('Checkout') {
            steps {
                // Checkout code from the GitHub repository
                git url: 'https://github.com/danielhasid/GUI_docker.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Install Python dependencies
                sh 'pip install -r reqs.txt'
            }
        }

        stage('Test') {
            steps {
                // Run tests
                sh 'pytest'
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
