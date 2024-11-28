pipeline {
    agent any
    environment {
        // Définir l'URL du webhook Discord et le message
        discordWebhookUrl = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
        payload = '{"content": "Test du webhook Discord"}'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Codacy Analysis') {
            steps {
                echo 'Performing Codacy analysis...'
            }
        }
        stage('Notify Discord') {
            steps {
                echo 'Notifying Discord...'
                script {
                    // Utiliser PowerShell pour envoyer la notification à Discord
                    powershell '''
                    $headers = @{ 'Content-Type' = 'application/json' }
                    $body = '${payload}'
                    Invoke-RestMethod -Uri '${discordWebhookUrl}' -Method Post -Headers $headers -Body $body
                    '''
                }
            }
        }
        stage('Deployment') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
    post {
        failure {
            echo 'The build or deployment failed.'
        }
        success {
            echo 'The build or deployment succeeded.'
        }
    }
}
