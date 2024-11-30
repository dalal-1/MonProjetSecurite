pipeline {
    agent any
    environment {
        ZAP_PORT = '8081'
        ZAP_REPORT_DIR = '/var/lib/jenkins/zap_reports'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Preparation') {
            steps {
                script {
                    // Met à jour et installe Nmap
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y nmap'
                }
            }
        }
        stage('Scan with Nmap') {
            steps {
                script {
                    // Effectue un scan Nmap sur les ports spécifiés
                    sh 'sudo nmap -p 80,443,8080 127.0.0.1'
                }
            }
        }
        stage('ZAP Scan') {
            steps {
                script {
                    // Vérifie que le répertoire pour les rapports existe et est accessible
                    sh 'sudo mkdir -p /var/lib/jenkins/zap_reports'
                    sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/zap_reports'
                    sh 'sudo chmod -R 755 /var/lib/jenkins/zap_reports'

                    // Effectue le scan ZAP et génère le rapport dans le répertoire approprié
                    sh 'sudo zaproxy -cmd -quickurl http://localhost:5000 -quickout /var/lib/jenkins/zap_reports/zap_report.html -port 8081'
                }
            }
        }
        stage('Post Actions') {
            steps {
                script {
                    // Exemple de nettoyage ou d'envoi de notification si nécessaire
                    echo 'Post actions completed'
                }
            }
        }
    }
    post {
        always {
            // Action qui s'exécute après la fin du pipeline (par exemple, nettoyage ou notifications)
            echo 'Pipeline finished'
        }
    }
}
