pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                bat 'npm install'  // Remplace par ta commande de build
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying the project..."
                bat 'deploy.bat'  // Remplace par ta commande de déploiement
            }
        }
    }
}
