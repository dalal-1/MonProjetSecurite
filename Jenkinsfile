pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'  // Votre URL Webhook Discord
    }

    stages {
        stage('Déclenchement du Checkout SCM') {
            steps {
                checkout scm  // Cloner votre dépôt Git ou autre source de code
            }
        }

        stage('Test Sécurité avec OWASP ZAP') {
            steps {
                script {
                    echo "Lancement du scan de sécurité OWASP ZAP..."

                    // Utilisation du plugin OWASP ZAP pour exécuter un scan
                    zapAttack(
                        apiKey: '',  // Laissez vide si vous n'utilisez pas de clé API
                        target: 'http://127.0.0.1:5000',  // URL de votre application à tester
                        zapOptions: [ '-config', 'api.disablekey=true' ]  // Désactive la clé API si nécessaire
                    )
                }
            }
        }

        stage('Envoyer Notification Discord') {
            steps {
                script {
                    echo "Envoi de la notification à Discord..."

                    // Créer la charge utile pour Discord
                    def payload = '{"content": "Le scan de sécurité OWASP ZAP est terminé avec succès!"}'
                    
                    // Envoi de la notification via Webhook Discord
                    httpRequest(
                        url: "${DISCORD_WEBHOOK_URL}",
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: payload
                    )
                }
            }
        }
    }

    post {
        failure {
            echo 'Le pipeline a échoué.'
            
            // Notification en cas d'échec
            script {
                def failurePayload = '{"content": "Le scan OWASP ZAP a échoué!"}'
                httpRequest(
                    url: "${DISCORD_WEBHOOK_URL}",
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    requestBody: failurePayload
                )
            }
        }
    }
}
