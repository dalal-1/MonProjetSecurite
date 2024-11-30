pipeline {
    agent any
    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Start Application') {
            steps {
                script {
                    echo 'Starting the application...'
                    sh 'python3 app.py'
                }
            }
        }
        stage('Run Nmap Scan') {
            steps {
                script {
                    echo 'Running Nmap scan...'

                    // Débogage pour vérifier l'utilisateur Jenkins
                    sh 'whoami'
                    sh 'sudo -v'  // Vérifie que sudo fonctionne sans mot de passe

                    // Exécution du scan Nmap avec sudo
                    def nmapResults = sh(script: 'sudo nmap -T4 -sS -p 80,443,8080 localhost', returnStdout: true).trim()
                    echo "Nmap Results: ${nmapResults}"

                    // Envoi des résultats à Discord (si nécessaire)
                    sendToDiscord("🚨 **Résultats Nmap** 🚨\n```\n${nmapResults}\n```")
                }
            }
        }
        stage('Run Nikto Scan') {
            steps {
                script {
                    echo 'Running Nikto scan...'
                    def niktoResults = sh(script: 'nikto -h localhost', returnStdout: true).trim()
                    echo "Nikto Results: ${niktoResults}"

                    // Envoi des résultats à Discord (si nécessaire)
                    sendToDiscord("🚨 **Résultats Nikto** 🚨\n```\n${niktoResults}\n```")
                }
            }
        }
        stage('Run ZAP Scan') {
            steps {
                script {
                    echo 'Running ZAP scan...'
                    // Assurez-vous que ZAP est installé et que zap-cli est utilisé pour exécuter le scan
                    def zapResults = sh(script: 'zap-cli quick-scan --self-contained localhost', returnStdout: true).trim()
                    echo "ZAP Results: ${zapResults}"

                    // Envoi des résultats à Discord (si nécessaire)
                    sendToDiscord("🚨 **Résultats ZAP** 🚨\n```\n${zapResults}\n```")
                }
            }
        }
        stage('Stop Application') {
            steps {
                script {
                    echo 'Stopping the application...'
                    sh 'kill $(lsof -t -i:5000)' // Assurez-vous de tuer le processus de l'application Flask si nécessaire
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

def sendToDiscord(message) {
    // Remplace cette fonction par l'intégration Discord que tu utilises pour envoyer des messages
    echo "Sending to Discord: ${message}"
    // Code d'envoi à Discord ici, par exemple avec un webhook
}
