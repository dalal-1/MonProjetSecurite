pipeline {
    agent any
    environment {
        // Utilisation de variables d'environnement Jenkins sécurisées pour éviter l'exposition des tokens
        DISCORD_WEBHOOK_URL_PIPELINE = credentials('discord-webhook-url')  // Assurez-vous d'ajouter 'discord-webhook-url' dans Jenkins secrets
        CODACY_TOKEN = credentials('codacy-token')  // Assurez-vous d'ajouter 'codacy-token' dans Jenkins secrets
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                script {
                    try {
                        // Commande de build, à remplacer par ta commande réelle si ce n'est pas Maven
                        sh 'mvn clean install -DskipTests'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                script {
                    try {
                        // Lancer les tests unitaires
                        sh 'mvn test'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Security Check') {
            steps {
                echo 'Running security analysis using Codacy...'
                script {
                    try {
                        // Lancer l'analyse Codacy
                        sh """
                        curl -X POST \
                            -H "Authorization: token ${CODACY_TOKEN}" \
                            -F "file=@${WORKSPACE}/your-project-file" \
                            https://api.codacy.com/2.0/coverage
                        """
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application to production...'
                script {
                    try {
                        // Déploiement avec Docker ou Kubernetes, ajuster la commande en fonction de votre configuration
                        sh 'docker-compose up -d'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded.'
            script {
                // Notification Discord pour une exécution réussie
                def payload = [
                    content: "🎉 Le pipeline Jenkins a **réussi** avec succès pour MonProjetSecurite!"
                ]
                def jsonPayload = groovy.json.JsonOutput.toJson(payload)
                sh """
                curl -X POST -H "Content-Type: application/json" -d '${jsonPayload}' ${DISCORD_WEBHOOK_URL_PIPELINE}
                """
            }
        }

        failure {
            echo 'Pipeline failed.'
            script {
                // Notification Discord pour une exécution échouée
                def payload = [
                    content: "🚨 Le pipeline Jenkins a **échoué** pour MonProjetSecurite. Veuillez vérifier les erreurs dans les logs."
                ]
                def jsonPayload = groovy.json.JsonOutput.toJson(payload)
                sh """
                curl -X POST -H "Content-Type: application/json" -d '${jsonPayload}' ${DISCORD_WEBHOOK_URL_PIPELINE}
                """
            }
        }

        always {
            echo 'Cleaning up workspace...'
            // Nettoyage de l'espace de travail après l'exécution du pipeline
            cleanWs()
        }
    }
}
