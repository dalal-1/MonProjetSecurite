pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add any build steps if necessary
            }
        }

        stage('Vulnerability Scan') {
            steps {
                echo 'Running Nmap Vulnerability Scan on HTTP service...'

                // Nmap command to scan the HTTP service on port 5000
                script {
                    def target = '127.0.0.1'  // Targeting localhost
                    def port = '5000'         // Default Flask port
                    
                    // Execute Nmap to detect HTTP vulnerabilities
                    bat "nmap -p ${port} --script=http-vuln* --open --reason ${target}"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add any deployment steps if necessary
            }
        }
    }
}
