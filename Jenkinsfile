pipeline {
    agent any

    environment {
        // URL du webhook Discord (remplacez avec votre URL)
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Start Flask Application') {
            steps {
                script {
                    echo 'Starting the Flask application...'
                    // Lancer l'application Flask en arrière-plan
                    sh 'python3 app.py &'
                    // Attendre un peu pour s'assurer que l'application est lancée
                    sleep 10
                }
            }
        }

        stage('Run Bandit Scan') {
            steps {
                script {
                    echo 'Running Bandit security scan...'
                    // Exécuter Bandit pour analyser le code source Python
                    def banditResults = sh(script: 'bandit -r .', returnStdout: true).trim()
                    echo "Bandit Results: ${banditResults}"
                    // Envoyer les résultats à Discord
                    sendToDiscord("🚨 **Bandit Scan Results** 🚨\n```\n${banditResults}\n```")
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    echo 'Running Nmap scan...'
                    // Exécuter un scan Nmap pour les ports ouverts
                    def nmapResults = sh(script: 'nmap -T4 -sS -p 80,443,8080 localhost', returnStdout: true).trim()
                    echo "Nmap Results: ${nmapResults}"
                    // Envoyer les résultats à Discord
                    sendToDiscord("🚨 **Nmap Scan Results** 🚨\n```\n${nmapResults}\n```")
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    echo 'Running ZAP security scan...'
                    // Exécuter un scan rapide avec ZAP Proxy (zaproxy)
                    def zapResults = sh(script: 'zaproxy -cmd -quickurl http://localhost:5000', returnStdout: true).trim()
                    echo "ZAP Results: ${zapResults}"
                    // Envoyer les résultats à Discord
                    sendToDiscord("🚨 **ZAP Scan Results** 🚨\n```\n${zapResults}\n```")
                }
            }
        }

        stage('Stop Flask Application') {
            steps {
                script {
                    echo 'Stopping the Flask application...'
                    // Arrêter l'application Flask
                    sh 'kill $(lsof -t -i:5000)'
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
