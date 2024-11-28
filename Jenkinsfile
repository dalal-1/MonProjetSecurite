pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the project code from the Git repository
                git 'https://github.com/dalal-1/MonProjetSecurite.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install dependencies (e.g., for Python)
                script {
                    // Use shell commands for installation
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (you can replace this with your specific testing command)
                script {
                    // For example, using pytest
                    sh 'pytest'
                }
            }
        }

        stage('Build') {
            steps {
                // Add your build steps here if needed (e.g., flask run, or other build steps)
                echo 'Building the project...'
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment commands here (e.g., using Ansible or other)
                echo 'Deploying the project...'
            }
        }
    }
}
