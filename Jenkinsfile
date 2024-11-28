pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
        TARGET_URL = 'http://127.0.0.1:5000/'  // URL de ton application Flask
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Vérifier si Nmap est installé (si nécessaire)
                    sh 'nmap --version'
                }
            }
        }

        stage('Run Nmap Security Test') {
            steps {
                script {
                    // Exécuter un scan Nmap sur l'URL cible
                    sh "nmap -sV ${TARGET_URL} -oX nmap_report.xml"
                }
            }
        }

        stage('Send Discord Notification') {
            steps {
                script {
                    // Message de notification à envoyer
                    def message = "Security test completed for ${TARGET_URL}.\nNmap Report saved at:\n${pwd()}/nmap_report.xml"
                    // Préparer le payload pour Discord
                    def payload = """
                    {
                        "content": "${message}"
                    }
                    """
                    // Envoi de la notification à Discord via webhook
                    sh """
                    curl -X POST -H "Content-Type: application/json" \
                    -d '${payload}' ${DISCORD_WEBHOOK_URL}
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
