pipeline {
    agent any
    environment {
        // URL Webhook Discord pour notifications du pipeline
        DISCORD_WEBHOOK_URL_PIPELINE = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
        
        // Token Codacy pour l'analyse de sécurité et de qualité du code
        CODACY_TOKEN = '01db00b69eac4393a4f5b8f081702953'
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
            node {
                cleanWs()
            }
        }
    }
}
