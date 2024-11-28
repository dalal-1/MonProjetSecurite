pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Vérifie que les sources du projet sont bien récupérées
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                // Place ici les étapes nécessaires pour la compilation ou la construction du projet
                // Par exemple, si tu utilises npm ou Maven :
                // bat 'npm install'  // Pour un projet Node.js
                // bat 'mvn clean install'  // Pour un projet Java/Maven
            }
        }

        stage('Codacy Analysis') {
            steps {
                echo "Performing Codacy analysis..."
                // Remplace ceci par les étapes spécifiques pour analyser ton projet avec Codacy
                // Exemple d'intégration Codacy avec GitHub et Jenkins :
                // bat 'curl -s https://www.codacy.com/project/{YOUR_PROJECT_TOKEN}/coverage-reports?token={YOUR_TOKEN}'
                // Assure-toi que tu as configuré l'outil Codacy ou un équivalent pour ton projet
            }
        }

        stage('Notify Discord') {
            steps {
                echo "Notifying Discord..."
                // Logic to notify Discord via Webhook
                script {
                    def discordWebhookUrl = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
                    def message = "Le pipeline Jenkins a été exécuté. Statut: ${currentBuild.currentResult}"
                    def payload = """
                    {
                        "content": "${message}"
                    }
                    """
                    
                    // Utilisation de PowerShell pour envoyer la requête HTTP POST
                    bat """
                    powershell -Command "\$headers = @{ 'Content-Type' = 'application/json' }; \$body = '${payload}'; Invoke-RestMethod -Uri '${discordWebhookUrl}' -Method Post -Headers \$headers -Body \$body"
                    """
                }
            }
        }

        stage('Deployment') {
            steps {
                echo "Deploying the application..."
                // Cette section est dédiée à l'automatisation du déploiement
                // Si tu utilises des outils comme Ansible ou Docker, intègre ici les commandes correspondantes
                // Exemple avec Docker (assure-toi d'avoir Docker configuré sur la machine) :
                // bat 'docker-compose up -d'
                // Si tu as des scripts de déploiement spécifiques, appelle-les ici
            }
        }
    }

    post {
        success {
            echo "The build and deployment were successful!"
        }

        failure {
            echo "The build or deployment failed."
        }
    }
}
d