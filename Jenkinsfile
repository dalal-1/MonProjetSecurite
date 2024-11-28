*pipeline {
    agent any
    stages {
        stage('Test PowerShell Webhook') {
            steps {
                script {
                    bat '''powershell -NoProfile -ExecutionPolicy Bypass -Command "
                        $headers = @{
                            'Content-Type' = 'application/json'
                        }
                        $body = '{"content": "Test du webhook Discord"}'
                        Invoke-RestMethod -Uri 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd' -Method Post -Headers $headers -Body $body
                    "'''
                }
            }
        }
    }
}
