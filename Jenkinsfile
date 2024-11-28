pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Nmap') {
            steps {
                bat 'echo %PATH%'
                bat 'nmap --version'
            }
        }

        stage('Vulnerability Scan') {
            steps {
                echo 'Running Nmap Vulnerability Scan on HTTP service...'
                script {
                    bat 'nmap -p 5000 --script=http-vuln* --open --reason 127.0.0.1'
                }
            }
        }
    }
}
