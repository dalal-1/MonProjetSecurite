pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies..."
                    sh 'pip install -r requirements.txt'
                }
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

        stage('Start ZAP for Security Scan') {
            steps {
                script {
                    echo "Starting ZAP for security scan..."
                    // Start OWASP ZAP in daemon mode for scanning
                    sh 'zap.sh -daemon -config api.disablekey=true'
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    echo "Running Nmap scan..."
                    // Run Nmap scan and save results to a variable
                    def nmapResults = sh(script: 'nmap -sS -p 80,443,8080 localhost', returnStdout: true).trim()
                    echo "Nmap Scan Results: ${nmapResults}"

                    // Send results to Discord
                    sendToDiscord("🚨 **Résultats des scans de sécurité** 🚨\n\n🔍 **Scan Nmap** :\nLes résultats du scan Nmap sont prêts. Voici les détails des ports ouverts et des services détectés sur le système :\n```\n${nmapResults}\n```\n_Analyse complète des services et des ports ouverts._ 🛠️")
                }
            }
        }

        stage('Run Nikto Scan') {
            steps {
                script {
                    echo "Running Nikto scan..."
                    // Run Nikto scan and save results to a variable
                    def niktoResults = sh(script: 'nikto -h http://localhost', returnStdout: true).trim()
                    echo "Nikto Scan Results: ${niktoResults}"

                    // Send results to Discord
                    sendToDiscord("🔒 **Scan Nikto** :\nNikto a détecté des vulnérabilités potentielles sur l'application web. Voici un résumé des problèmes identifiés :\n```\n${niktoResults}\n```\n_Exploration approfondie des vulnérabilités de l'application._ ⚠️")
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    echo "Running ZAP scan..."
                    // Run ZAP scan and save results to a variable
                    def zapResults = sh(script: 'zap-cli quick-scan --self-contained http://localhost', returnStdout: true).trim()
                    echo "ZAP Scan Results: ${zapResults}"

                    // Send results to Discord
                    sendToDiscord("🛡️ **Scan ZAP (OWASP)** :\nLe scan de sécurité effectué par ZAP a permis d\'identifier des failles potentielles et des risques liés à la sécurité de l\'application :\n```\n${zapResults}\n```\n_Analyse complète du code de l'application et de sa sécurité._ 🔐")
                }
            }
        }

        stage('Stop ZAP') {
            steps {
                script {
                    echo "Stopping ZAP..."
                    // Stop OWASP ZAP after scan is complete
                    sh 'zap.sh -daemon -config api.disablekey=true -stop'
                }
            }
        }

        stage('Stop Application') {
            steps {
                script {
                    echo "Stopping application..."
                    // Stop the Flask application
                    sh 'pkill -f app.py'
                }
            }
        }

        stage('Generate Reports') {
            steps {
                script {
                    echo "Generating reports..."
                    // Place any additional report generation steps here, if needed.
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    echo "Cleaning up workspace..."
                    cleanWs()
                }
            }
        }
    }

    post {
        always {
            // Send final completion message to Discord
            sendToDiscord("🔔 **Tous les scans ont été exécutés avec succès !**\nLes résultats sont maintenant disponibles pour examen et peuvent être utilisés pour renforcer la sécurité de l'application. Si vous avez des questions ou des préoccupations, n'hésitez pas à nous contacter. 📩\n\n**🔒 Sécurisez vos systèmes, protégez vos données !** 🛡️")
        }
    }
}

// Function to send messages to Discord webhook
def sendToDiscord(String message) {
    sh """
    curl -X POST -H "Content-Type: application/json" \
    -d '{"content": "${message}"}' \
    ${DISCORD_WEBHOOK_URL}
    """
}
