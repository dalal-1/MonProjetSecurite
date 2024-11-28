pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'  // Lien de ton dépôt Git
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'  // Webhook Discord
    }

    triggers {
        // Déclenchement automatique à chaque changement sur la branche 'main' du dépôt
        githubPush()  // Déclenche automatiquement le pipeline lors d'un push sur GitHub
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupération du code depuis GitHub
                git url: "${GIT_REPO}", branch: 'main'
            }
        }

        stage('Build') {
            steps {
                // Compilation et préparation de l'application
                echo 'Building the application...'
                // Ajoute ici les commandes de build comme 'mvn clean install' ou autres
            }
        }

        stage('Deploy') {
            steps {
                // Déploiement de l'application
                echo 'Deploying the application...'
                // Ajoute les commandes nécessaires pour déployer ton application
            }
        }

        stage('Test') {
            steps {
                // Tests automatisés
                echo 'Running tests...'
                // Ajoute ici les commandes pour exécuter les tests
            }
        }

        stage('Security Check') {
            steps {
                // Vérification de la sécurité
                echo 'Running security checks...'
                // Ajoute les outils de vérification comme OWASP ZAP ou SonarQube
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Ajoute ici des étapes pour le nettoyage après l'exécution
        }
        success {
            echo 'Build, Deploy, Test, and Security Check completed successfully.'
            // Notification Discord sur succès
            script {
                def message = "✅ **Pipeline Success**\nBuild, deploy, tests, and security checks were completed successfully."
                sendDiscordNotification(message)
            }
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
            // Notification Discord sur échec
            script {
                def message = "❌ **Pipeline Failed**\nAn error occurred during the pipeline execution. Check logs for details."
                sendDiscordNotification(message)
            }
        }
    }
}

def sendDiscordNotification(String message) {
    // Fonction pour envoyer un message à Discord
    def payload = """{
        "content": "${message}"
    }"""
    
    // Envoie la requête POST à Discord via le webhook
    sh """
        curl -X POST -H "Content-Type: application/json" -d '${payload}' ${DISCORD_WEBHOOK_URL}
    """
}
