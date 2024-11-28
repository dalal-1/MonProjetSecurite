pipeline {
    agent any

    environment {
        // Configuration pour la notification Discord
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                git 'https://github.com/dalal-1/MonProjetSecurite.git'  // Remplacez par votre dépôt
            }
        }

        stage('Installation des dépendances') {
            steps {
                script {
                    sh 'npm install'  // Ou pip install si c'est un projet Python
                }
            }
        }

        stage('Lancer les tests OWASP ZAP') {
            steps {
                script {
                    // Démarre OWASP ZAP pour effectuer un test de sécurité sur l'URL donnée
                    sh '''
                    zap-baseline.py -t http://127.0.0.1:5000/ -g gen.conf -r zap_report.html
                    '''
                }
            }
        }

        stage('Analyser le rapport de sécurité') {
            steps {
                script {
                    // Vérification du rapport de ZAP
                    def zapReport = readFile('zap_report.html')
                    // Ajouter ici votre logique pour analyser le rapport (ex: rechercher des vulnérabilités)
                    if (zapReport.contains("High")) {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Envoyer une notification à Discord') {
            steps {
                script {
                    def message = "Le pipeline a échoué lors des tests de sécurité."
                    if (currentBuild.result == 'SUCCESS') {
                        message = "Le pipeline a réussi. Aucun problème de sécurité détecté."
                    }

                    def payload = [
                        'content': message
                    ]
                    // Envoi de la notification à Discord
                    sh """
                    curl -X POST -H "Content-Type: application/json" \
                    -d '${payload}' \
                    https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
    }
}
