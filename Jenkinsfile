pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    sendDiscordNotification('Checkout completed successfully!')
                }
            }
        }

        stage('Check Nmap') {
            steps {
                bat 'echo %PATH%'
                bat 'nmap --version'
                script {
                    sendDiscordNotification('Nmap is installed and version verified.')
                }
            }
        }

        stage('Vulnerability Scan with Nmap') {
            steps {
                echo 'Running Nmap Vulnerability Scan on HTTP service...'
                bat 'nmap -p 5000 --script=http-vuln* --open --reason 127.0.0.1'
                script {
                    sendDiscordNotification('Nmap vulnerability scan completed for HTTP service on port 5000.')
                }
            }
        }

        stage('Run scan.py') {
            steps {
                echo 'Running scan.py for additional vulnerability checks...'
                script {
                    // Assuming the Python environment is set up and scan.py is in the project directory
                    sh 'python3 scan.py'
                    sendDiscordNotification('security_scan.py execution completed.')
                }
            }
        }
    }

    post {
        always {
            script {
                sendDiscordNotification('Pipeline execution finished.')
            }
        }
    }
}

// Function to send a notification to Discord
def sendDiscordNotification(String message) {
    def body = """
    {
        "content": "$message"
    }
    """
    def response = httpRequest(
        acceptType: 'APPLICATION_JSON',
        contentType: 'APPLICATION_JSON',
        httpMode: 'POST',
        url: env.DISCORD_WEBHOOK_URL,
        requestBody: body
    )
}
