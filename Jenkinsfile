pipeline {
    agent any

    environment {
        // Définir les variables d'environnement nécessaires
        SSH_AGENT = credentials('delaila')  // S'assurer que le credential "delaila" est correctement configuré
    }

    stages {
        stage('Checkout') {
            steps {
                // Cloner le projet depuis GitHub
                git 'https://github.com/dalal-1/MonProjetSecurite.git'
            }
        }

        stage('Initialize ZAP') {
            steps {
                // Initialisation de l'agent SSH
                sshagent(['delaila']) {
                    sh '''
                        echo "Initialisation de ZAP"
                        # Ajoutez ici toute commande nécessaire pour démarrer ZAP ou configurer les tests
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline terminé"
        }
        success {
            echo "Pipeline réussi"
        }
        failure {
            echo "Pipeline échoué"
        }
    }
}
