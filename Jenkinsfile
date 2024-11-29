pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'  // Remplace par ton URL de dépôt Git
        TARGET_URL = 'https://localhost:5000'  // URL cible à tester, modifie selon ton besoin
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'  // Ton webhook Discord
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Récupérer le code du projet depuis le dépôt Git
                git url: "${GIT_REPO}", branch: 'main'  // Remplace 'main' par la branche que tu utilises
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Installer les dépendances nécessaires (si Python ou autres bibliothèques sont nécessaires)
                    sh '''
                    # Mettre à jour les packages
                    sudo apt-get update

                    # Installer les dépendances Python (si non installées)
                    pip install requests
                    '''
                }
            }
        }

        stage('Run Security Scan') {
            steps {
                script {
                    // Exécuter le script Python de sécurité
                    echo "Running Security Scan..."
                    sh 'python3 security_scan.py'
                }
            }
        }

        stage('Notify Discord') {
            steps {
                script {
                    // Notification via Discord
                    def message = 'Security scan completed.'

                    // Envoie un message à Discord via le webhook
                    sh """
                    curl -X POST -H "Content-Type: application/json" \
                        -d '{"content": "${message}"}' \
                        ${DISCORD_WEBHOOK_URL}
                    """
                }
            }
        }
    }

    post {
        always {
            // Actions après l'exécution, comme nettoyer ou notifier en cas d'échec
            echo 'Pipeline finished.'
        }

        success {
            // Si le pipeline est réussi, envoie une notification de succès
            echo 'Pipeline completed successfully.'
        }

        failure {
            // Si le pipeline échoue, envoie une notification d'erreur
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}
