pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
        ZAP_URL = 'http://localhost:9090'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    // Vérifier si le dépôt Git est correctement configuré
                    git branch: 'main', url: 'https://github.com/dalal-1/MonProjetSecurite.git'
                }
            }
        }

        stage('Installation des dépendances') {
            steps {
                script {
                    // Installer les dépendances nécessaires pour l'application (assurez-vous que votre fichier requirements.txt existe)
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Lancer les tests OWASP ZAP') {
            steps {
                script {
                    // Lancer l'analyse de sécurité OWASP ZAP
                    sh 'curl -X POST "$ZAP_URL/JSON/ascan/action/scan"'
                }
            }
        }

        stage('Analyser le rapport de sécurité') {
            steps {
                script {
                    // Analyser le rapport de sécurité généré par OWASP ZAP
                    sh 'curl -X GET "$ZAP_URL/JSON/core/view/alerts"'
                }
            }
        }

        stage('Envoyer une notification à Discord') {
            steps {
                script {
                    // Envoyer une notification sur Discord avec les résultats de l'analyse
                    sh '''
                    curl -X POST -H "Content-Type: application/json" -d '{
                        "content": "Les tests de sécurité sont terminés. Veuillez consulter les résultats."
                    }' $DISCORD_WEBHOOK
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
        success {
            echo 'Pipeline exécuté avec succès.'
        }
        failure {
            echo 'Erreur dans le pipeline.'
        }
    }
}
