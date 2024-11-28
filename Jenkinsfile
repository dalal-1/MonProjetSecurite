pipeline {
    agent any  // Utiliser 'any' pour exécuter sur n'importe quel agent disponible

    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'  // URL du dépôt Git
        DISCORD_WEBHOOK_URL = 'your-discord-webhook-url'  // Webhook Discord (remplacer par le vôtre)
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                // Cloner le code depuis le dépôt Git
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Exemple pour un projet Maven : Compiler le projet avec Maven
                sh 'mvn clean install'  // Remplacer par la commande appropriée selon votre projet
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Exemple pour exécuter des tests avec Maven
                sh 'mvn test'  // Remplacer par vos tests, ou utiliser un autre framework de test
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                // Exemple de déploiement avec Docker (remplacer par votre méthode de déploiement)
                sh 'docker-compose up -d'  // Utiliser docker-compose ou toute autre méthode pour déployer
            }
        }

        stage('Security Checks') {
            steps {
                echo 'Performing security checks...'
                // Exemple d'utilisation de OWASP ZAP pour effectuer un scan de sécurité
                // Assurez-vous d'avoir OWASP ZAP installé ou d'utiliser un container Docker pour le scanner
                sh './zap-cli quick-scan --self-contained --url http://localhost:8080'  // Remplacer par l'URL de votre application
            }
        }

        stage('Post-deployment') {
            steps {
                echo 'Performing post-deployment steps...'
                // Par exemple, vous pouvez faire des vérifications supplémentaires ou réactiver des services
                sh 'echo "Post-deployment checks completed."'
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up the workspace...'
            cleanWs()  // Nettoyage de l'espace de travail après l'exécution du pipeline
        }
        
        success {
            echo 'Pipeline executed successfully!'
            // Envoi d'une notification de succès à Discord
            script {
                def payload = [
                    content: "Pipeline executed successfully: ${currentBuild.fullDisplayName}"
                ]
                sh """
                curl -X POST -H "Content-Type: application/json" -d '${groovy.json.JsonOutput.toJson(payload)}' ${DISCORD_WEBHOOK_URL}
                """
            }
        }
        
        failure {
            echo 'Pipeline failed.'
            // Envoi d'une notification d'échec à Discord
            script {
                def payload = [
                    content: "Pipeline failed: ${currentBuild.fullDisplayName}"
                ]
                sh """
                curl -X POST -H "Content-Type: application/json" -d '${groovy.json.JsonOutput.toJson(payload)}' ${DISCORD_WEBHOOK_URL}
                """
            }
        }
    }
}
