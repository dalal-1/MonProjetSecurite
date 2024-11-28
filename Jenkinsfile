pipeline {
    agent any

    environment {
        NMAP_PATH = "C:\\Program Files (x86)\\Nmap" // Path to Nmap on your Windows machine
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
                    // Assuming you run an Nmap scan and save the result
                    def scanResult = bat(script: 'nmap -p 80 --script vuln <TARGET_IP>', returnStdout: true).trim()
                    
                    // Check if the scan has vulnerabilities
                    def scanDetails = scanResult.contains("Vulnerabilities found") ? scanResult : "No vulnerabilities found during the scan."
                    
                    // Send the results to Discord
                    def message = """
                    {
                        "content": "Vulnerability scan completed. Here are the details:\n${scanDetails}"
                    }
                    """
                    // Post to Discord webhook
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
                    // Notify that the job has completed
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
