pipeline {
    agent any

    environment {
        PATH = "${tool 'Git'}:/usr/local/bin:/usr/bin:/bin:C:\\Program Files\\Jenkins\\bin"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Ajoutez ici vos étapes de build, comme la compilation ou l'installation des dépendances
            }
        }

        stage('Codacy Analysis') {
            steps {
                echo 'Performing Codacy analysis...'
                // Ajoutez ici vos étapes d'analyse avec Codacy si nécessaire
            }
        }

        stage('Notify Discord') {
            steps {
                echo 'Notifying Discord...'
                // Ajoutez ici vos étapes pour notifier Discord
            }
        }

        stage('Powershell Test') {
            steps {
                echo 'Running PowerShell script...'
                // Exécuter le script PowerShell avec le chemin absolu
                powershell '"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "echo Hello World"'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application...'
                // Ajoutez ici vos étapes de déploiement
            }
        }
    }

    post {
        failure {
            echo 'The build or deployment failed.'
        }
    }
}
