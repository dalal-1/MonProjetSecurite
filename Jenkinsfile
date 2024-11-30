pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd"
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Preparation') {
            steps {
                script {
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y nmap'
                    sendDiscordNotification("🔧 **Preparation complète** ✅\nLes dépendances ont été mises à jour et Nmap installé!")
                }
            }
        }

        stage('Scan with Nmap') {
            steps {
                script {
                    sh 'sudo nmap -p 80,443,8080 127.0.0.1'
                    sendDiscordNotification("🛠️ **Scan Nmap terminé** 🕵️‍♂️\nLes ports ont été scannés : 80/tcp (closed), 443/tcp (closed), 8080/tcp (open).")
                }
            }
        }

        stage('ZAP Scan') {
            steps {
                script {
                    sh 'sudo mkdir -p /var/lib/jenkins/zap_reports'
                    sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/zap_reports'
                    sh 'sudo chmod -R 755 /var/lib/jenkins/zap_reports'
                    sh 'sudo zaproxy -cmd -quickurl http://localhost:5000 -quickout /var/lib/jenkins/zap_reports/zap_report.html -port 8081'
                    sendDiscordNotification("🚨 **Scan ZAP terminé** ✅\nLe rapport de sécurité a été généré :zap: [Clique ici pour le rapport](file:///var/lib/jenkins/zap_reports/zap_report.html).")
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    echo "Post actions completed"
                    sendDiscordNotification("🎉 **Pipeline terminé avec succès!** 🎉\nToutes les étapes ont été réalisées sans erreur!")
                }
            }
        }
    }

    post {
        always {
            sendDiscordNotification("🔔 **Pipeline exécuté**: ${currentBuild.result} - ${env.BUILD_URL}")
        }
    }
}

def sendDiscordNotification(String message) {
    sh """
        curl -X POST -H "Content-Type: application/json" \
        -d '{"content": "${message}"}' \
        ${DISCORD_WEBHOOK_URL}
    """
}
