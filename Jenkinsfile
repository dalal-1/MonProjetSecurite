pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Show Current Directory') {
            steps {
                script {
                sh 'pwd'  // Affiche le répertoire courant
        }
    }
}


        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Nmap') {
            steps {
                script {
                    bat 'echo C:\\Windows\\System32;C:\\Program Files\\Git\\bin;C:\\Program Files (x86)\\Nmap'
                    bat 'nmap --version'
                }
            }
        }

        stage('Vulnerability Scan') {
            steps {
                script {
                    echo 'Running Nmap Vulnerability Scan on HTTP service...'
                    // Placeholder for actual Nmap scan command
                    def nmapResults = 'Scan results here'

                    // Creating JSON payload for Discord notification
                    def body = """
                    {
                        "content": "Nmap vulnerability scan completed for HTTP service on port 5000."
                    }
                    """
                    echo "Sending message: $body"

                    // Sending HTTP request to Discord
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: env.DISCORD_WEBHOOK_URL,
                        requestBody: body
                    )
                }
            }
        }

        stage('Declarative: Post Actions') {
            steps {
                script {
                    def body = """
                    {
                        "content": "Pipeline completed successfully!"
                    }
                    """
                    // Sending a post-pipeline completion notification to Discord
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: env.DISCORD_WEBHOOK_URL,
                        requestBody: body
                    )
                }
            }
        }
    }
}

