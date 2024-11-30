pipeline {
    agent any

    environment {
        // URL du webhook Discord
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Run Bandit Scan') {
            steps {
                script {
                    // Exécuter Bandit pour analyser le code Python et continuer même si des erreurs sont détectées
                    def banditResults = sh(script: 'bandit -r .', returnStdout: true, returnStatus: true).trim()
                    echo "Bandit Results: ${banditResults}"
                    sendToDiscord("🚨 **Bandit Scan Results** 🚨\n```\n${banditResults}\n```")
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    // Exécuter un scan Nmap pour les ports ouverts sur localhost
                    def nmapResults = sh(script: 'nmap -T4 -sS -p 80,443 localhost', returnStdout: true).trim()
                    echo "Nmap Results: ${nmapResults}"
                    sendToDiscord("🚨 **Nmap Scan Results** 🚨\n```\n${nmapResults}\n```")
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    // Exécuter un scan rapide avec ZAP
                    def zapResults = sh(script: 'zaproxy -cmd -quickurl http://localhost:5000', returnStdout: true).trim()
                    echo "ZAP Results: ${zapResults}"
                    sendToDiscord("🚨 **ZAP Scan Results** 🚨\n```\n${zapResults}\n```")
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Nettoyage de l'espace de travail après l'exécution
        }
    }
}

// Fonction pour envoyer un message à Discord via Webhook
def sendToDiscord(message) {
    sh """
        curl -X POST -H "Content-Type: application/json" \
        -d '{"content": "${message}"}' \
        ${DISCORD_WEBHOOK_URL}
    """
}
