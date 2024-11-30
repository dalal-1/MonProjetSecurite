pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/ton-webhook'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Start Application') {
            steps {
                script {
                    echo "Starting the application..."
                    sh 'python3 app.py &'
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    echo "Running Nmap scan..."
                    // Scan les ports 80, 443, et 8080
                    def nmapResults = sh(script: 'nmap -T4 -sS -p 80,443,8080 localhost', returnStdout: true).trim()
                    echo "Nmap Results: ${nmapResults}"

                    // Envoie les résultats à Discord
                    sendToDiscord("🚨 **Résultats Nmap** 🚨\n```\n${nmapResults}\n```")
                }
            }
        }

        stage('Run Nikto Scan') {
            steps {
                script {
                    echo "Running Nikto scan..."
                    // Scan Nikto sur l'application
                    def niktoResults = sh(script: 'nikto -h http://localhost', returnStdout: true).trim()
                    echo "Nikto Results: ${niktoResults}"

                    // Envoie les résultats à Discord
                    sendToDiscord("🔒 **Résultats Nikto** 🔒\n```\n${niktoResults}\n```")
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    echo "Running ZAP scan..."
                    // Exécute un scan rapide avec zap-cli
                    def zapResults = sh(script: 'zap-cli quick-scan --self-contained http://localhost', returnStdout: true).trim()
                    echo "ZAP Results: ${zapResults}"

                    // Envoie les résultats à Discord
                    sendToDiscord("🛡️ **Résultats ZAP** 🛡️\n```\n${zapResults}\n```")
                }
            }
        }

        stage('Stop Application') {
            steps {
                script {
                    echo "Stopping the application..."
                    // Arrête l'application Flask
                    sh 'pkill -f app.py'
                }
            }
        }
    }

    post {
        always {
            // Nettoyage de l'espace de travail
            cleanWs()
        }
    }
}

// Fonction pour envoyer un message à Discord
def sendToDiscord(String message) {
    sh """
    curl -X POST -H "Content-Type: application/json" \
    -d '{"content": "${message}"}' \
    ${DISCORD_WEBHOOK_URL}
    """
}
