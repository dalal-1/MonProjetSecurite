pipeline {
    agent any
    stages {
        stage('Test Sécurité avec OWASP ZAP') {
            steps {
                script {
                    // URL cible pour tester
                    def targetUrl = 'http://localhost:8080'  // Modifiez l'URL cible selon votre besoin
                    def zapUrl = 'http://localhost:8080'     // URL de votre instance ZAP

                    // Lancement de ZAP dans Docker si vous n'avez pas ZAP localement installé
                    sh '''
                        docker run -u zap -p 8080:8080 owasp/zap2docker-stable
                    '''

                    // Attente pour que ZAP soit prêt
                    sleep(time: 20, unit: 'SECONDS')

                    // Lancer le scan de sécurité avec ZAP
                    def zapScan = sh(script: "curl -X GET ${zapUrl}/JSON/ascan/action/scan?url=${targetUrl}", returnStdout: true).trim()

                    // Vérifier si une vulnérabilité a été détectée
                    if (zapScan.contains('alert')) {
                        error 'Vulnérabilité détectée avec OWASP ZAP!'
                    } else {
                        echo 'Aucune vulnérabilité détectée.'
                    }
                }
            }
        }
        stage('Envoyer Notification Discord') {
            steps {
                script {
                    // URL Webhook Discord
                    def webhookUrl = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
                    
                    // Message de notification
                    def message = '{"content": "Le test de sécurité a terminé. Aucune vulnérabilité détectée."}'

                    // Si une vulnérabilité est détectée
                    if (currentBuild.result == 'FAILURE') {
                        message = '{"content": "Alerte : Vulnérabilité détectée par OWASP ZAP lors du test de sécurité!"}'
                    }

                    // Envoi de la notification à Discord
                    def curlCommand = "curl -X POST -H 'Content-Type: application/json' -d '${message}' ${webhookUrl}"
                    sh curlCommand
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
