pipeline {
    agent any

    environment {
        // Codacy Project Token
        CODACY_PROJECT_TOKEN = '01db00b69eac4393a4f5b8f081702953'
        // Webhook URL for Discord notifications
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Checkout') {
            steps {
                // Retrieve the code from GitHub
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add the steps necessary to build your project here.
                // For example, if it's a Maven project: sh 'mvn clean install'
            }
        }

        stage('Codacy Analysis') {
            steps {
                script {
                    // Install Codacy coverage tool
                    sh 'curl -sS https://coverage.codacy.com/get.sh | bash'
                    
                    // Upload the coverage report to Codacy
                    sh """
                    curl -X POST -H 'Content-Type: application/json' -d '{
                        "token": "${env.CODACY_PROJECT_TOKEN}",
                        "branch": "main"
                    }' https://api.codacy.com/2.0/coverage
                    """
                }
            }
        }

        stage('Notify Discord') {
            steps {
                script {
                    // Check the status of the build
                    def status = currentBuild.currentResult
                    def message = status == 'SUCCESS' ? "The build was successful!" : "The build failed."

                    // Send a Discord notification with the build status
                    sh """
                    curl -H "Content-Type: application/json" \
                         -X POST \
                         -d '{"content": "Pipeline Status: ${message}"}' \
                         ${env.DISCORD_WEBHOOK_URL}
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Check the logs for errors.'
        }
    }
}
