pipeline {
    agent any
    
    stages {
        stage('Preparation') {
            steps {
                script {
                    // Par exemple, installer nmap avec sudo si nécessaire
                    sh 'sudo apt-get update && sudo apt-get install -y nmap'
                }
            }
        }
        
        stage('Scan with Nmap') {
            steps {
                script {
                    // Lancer nmap sur un port spécifique avec sudo
                    sh 'sudo nmap -p 80,443,8080 127.0.0.1'
                }
            }
        }
        
        stage('ZAP Scan') {
            steps {
                script {
                    // Lancer ZAP avec le port spécifié (8081 ici)
                    sh 'sudo zaproxy -cmd -quickurl http://localhost:5000 -quickout zap_report.html -port 8081'
                }
            }
        }
        
        stage('Post Actions') {
            steps {
                script {
                    // Exécution des actions après le scan (exemple)
                    sh 'chmod +x post_actions.sh && ./post_actions.sh'
                }
            }
        }
    }
}
