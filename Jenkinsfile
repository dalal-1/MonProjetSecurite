pipeline {
    agent any
    stages {
        stage('Test Sécurité') {
            steps {
                script {
                    // Exemple d'un test de sécurité basique : vérifier si le port 80 est ouvert
                    def result = bat(script: 'netstat -an | findstr ":80"', returnStatus: true)
                    if (result != 0) {
                        error 'Port 80 fermé - Test de sécurité échoué!'
                    } else {
                        echo 'Port 80 ouvert - Test de sécurité réussi'
                    }
                }
            }
        }
        stage('Envoyer Notification') {
            steps {
                script {
                    // Envoyer une notification Discord
                    def webhookUrl = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
                    def message = '{"content": "Le test de sécurité est réussi et le pipeline est terminé."}'
                    def curlCommand = "curl -X POST -H 'Content-Type: application/json' -d '${message}' ${webhookUrl}"
                    bat script: curlCommand
                }
            }
        }
    }
    post {
        success {
            echo 'Le pipeline a réussi.'
        }
        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
