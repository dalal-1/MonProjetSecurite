pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Run Bandit Scan') {
            steps {
                script {
                    // Exécute Bandit sur le répertoire du projet et récupère uniquement la sortie
                    def banditResults = sh(script: 'bandit -r .', returnStdout: true).trim()
                    echo "Bandit scan results: ${banditResults}"
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    // Exécute Nmap pour scanner les ports 80 et 443 sur localhost
                    def nmapResults = sh(script: 'nmap -T4 -sS -p 80,443 localhost', returnStdout: true).trim()
                    echo "Nmap scan results: ${nmapResults}"
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    // Exécute ZAP pour scanner le site web local (assurez-vous que ZAP est configuré)
                    def zapResults = sh(script: 'zaproxy -cmd -quickurl http://localhost:5000', returnStdout: true).trim()
                    echo "ZAP scan results: ${zapResults}"
                }
            }
        }

        stage('Post Actions') {
            steps {
                cleanWs() // Nettoie le répertoire de travail à la fin du pipeline
            }
        }
    }
}
