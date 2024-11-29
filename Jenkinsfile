pipeline {
    agent any

    environment {
        SSH_AGENT = credentials('delaila')  // Utilise le credential 'delaila' contenant la clé privée SSH
    }

    stages {
        stage('Checkout') {
            steps {
                // Cloner le projet en utilisant l'URL SSH et le credential 'delaila'
                git credentialsId: 'delaila', url: 'git@github.com:dalal-1/MonProjetSecurite.git'
            }
        }

        stage('Initialize ZAP') {
            steps {
                // Initialisation de l'agent SSH
                sshagent(['delaila']) {
                    sh '''
                        echo "Initialisation de ZAP"
                        # Ajoutez ici les commandes nécessaires pour démarrer ZAP ou configurer les tests
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
