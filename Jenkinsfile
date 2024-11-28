pipeline {
    agent any
    
    environment {
        // URL de votre serveur Discord pour les notifications
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
        TARGET_URL = 'http://127.0.0.1:5000' // URL de votre application Flask
    }
    
    stages {
        stage('Start ZAP in Daemon Mode') {
            steps {
                script {
                    // Lancer ZAP en mode daemon avec un port spécifique
                    bat "start /B C:\\Program Files\\ZAP\\Zed Attack Proxy\\zap.bat -daemon -port 9090"
                    sleep(10) // Attendre que ZAP démarre
                }
            }
        }
        
        stage('Run ZAP Security Scan') {
            steps {
                script {
                    // Utiliser l'API de ZAP pour effectuer un scan sur l'application locale
                    bat "curl -X GET 'http://localhost:9090/JSON/ascan/action/scan/?url=${TARGET_URL}'"
                    sleep(60) // Attendre que le scan soit effectué
                }
            }
        }

        stage('Send Discord Notification') {
            steps {
                script {
                    // Préparer le message JSON pour Discord
                    def message = """{
                        "content": "Scan OWASP ZAP terminé pour l'application Flask : ${TARGET_URL}"
                    }"""
                    
                    // Envoyer une notification à Discord via le webhook
                    httpRequest(
                        url: "${DISCORD_WEBHOOK_URL}",
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: message
                    )
                }
            }
        }
    }
    
    post {
        always {
            // Fermer ZAP après le scan
            bat "taskkill /F /IM zap.exe"
        }
    }
}
