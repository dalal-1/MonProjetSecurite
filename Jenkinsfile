pipeline {
    agent any

    environment {
        NMAP_PATH = "C:\\Program Files (x86)\\Nmap" // Path to Nmap on your Windows machine
        TARGET_URL = "http://127.0.0.1:5000/" // Target Flask app URL
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Check Nmap') {
            steps {
                bat 'echo C:\\Windows\\System32;C:\\Program Files\\Git\\bin;C:\\Program Files (x86)\\Nmap'
                bat 'nmap --version'
            }
        }

        stage('Vulnerability Scan') {
            steps {
                script {
                    // Perform a simple vulnerability scan on the Flask application
                    def scanResult = bat(script: "nmap -p 5000 --script vuln ${TARGET_URL}", returnStdout: true).trim()

                    // Check if vulnerabilities are found
                    def scanDetails = scanResult.contains("Vulnerabilities found") ? scanResult : "No vulnerabilities found during the scan."
                    
                    // Send the scan results to Discord webhook
                    def message = """
                    {
                        "content": "Vulnerability scan completed for ${TARGET_URL}. Here are the details:\n${scanDetails}"
                    }
                    """
                    // Post the message to Discord
                    httpRequest(
                        url: 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd',
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: message
                    )
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    // Notify that the Jenkins job has completed
                    def completionMessage = """
                    {
                        "content": "The Jenkins pipeline has completed. Check the scan results above."
                    }
                    """
                    httpRequest(
                        url: 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd',
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: completionMessage
                    )
                }
            }
        }
    }
}
