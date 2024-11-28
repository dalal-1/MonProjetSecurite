pipeline {
    agent any
    
    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/<WEBHOOK_ID>'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning the repository..."
                git url: "${GIT_REPO}", branch: 'main'  // Spécifie la branche 'main'
            }
        }
        
        stage('Build') {
            steps {
                echo "Building the project..."
                // Remplace cette ligne avec la commande de build spécifique à ton projet
                bat 'npm install'  // Exemple pour un projet Node.js
            }
        }
        
        stage('Codacy Analysis') {
            steps {
                echo "Performing Codacy analysis..."
                // Ajouter votre code pour l'analyse Codacy ici, si applicable
            }
        }
        
        stage('Notify Discord') {
            steps {
                echo "Notifying Discord..."
                script {
                    def message = '{"content":"Build complete and deployment successful!"}'
                    // Envoi de la notification Discord
                    bat "curl -X POST -H \"Content-Type: application/json\" -d \"${message}\" ${DISCORD_WEBHOOK_URL}"
                }
            }
        }
        
        stage('Deployment') {
            steps {
                echo "Deploying the application..."
                // Ajoute tes commandes de déploiement ici
            }
        }

        stage('Post Actions') {
            steps {
                echo "The build and deployment were successful!"
            }
        }
    }

    triggers {
        // Configuration pour déclencher automatiquement le build sur un push Git
        githubPush()  // Déclenche le pipeline à chaque push dans GitHub
    }
}
