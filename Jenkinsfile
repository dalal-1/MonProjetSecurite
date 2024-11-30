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
                    sendDiscordNotification("🔧 **Étape 1 : Préparation Terminée** ✅\nLa mise à jour des dépendances a été effectuée et Nmap a été installé avec succès. Prêt à lancer le scan !")
                }
            }
        }

        stage('Scan with Nmap') {
            steps {
                script {
                    sh 'sudo nmap -p 80,443,8080 127.0.0.1 -oN /var/lib/jenkins/nmap_scan_results.txt'
                    def nmapResults = sh(script: 'cat /var/lib/jenkins/nmap_scan_results.txt', returnStdout: true).trim()
                    def nmapMessage = """
                    🛠️ **Étape 2 : Scan Nmap Terminé** 🕵️‍♂️
                    Le scan des ports a été effectué avec succès.
                    Résumé des résultats :
                    
                    ```txt
                    ${nmapResults}
                    ```
                    
                    Les détails complets sont enregistrés dans un fichier texte.
                    """
                    sendDiscordNotification(nmapMessage)
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
                    sendDiscordNotification("🚨 **Étape 3 : Scan ZAP Terminé** ✅\nLe scan de sécurité a été effectué avec succès. Le rapport détaillé est disponible.\n\n🔑 **Rapport de sécurité ZAP** : [Rapport HTML](file:///var/lib/jenkins/zap_reports/zap_report.html).")
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    echo "Toutes les étapes du pipeline sont terminées."
                    sendDiscordNotification("🎉 **Pipeline Terminée avec succès !** 🎉\nToutes les étapes ont été exécutées sans erreur et les rapports ont été générés.")
                }
            }
        }
    }

    post {
        always {
            script {
                def result = currentBuild.result ?: 'SUCCESS'
                def pipelineMessage = """
                🔔 **Exécution du Pipeline : ${result}**
                Consultez les résultats ici : ${env.BUILD_URL}
                """
                sendDiscordNotification(pipelineMessage)
            }
        }
    }
}

def sendDiscordNotification(String message) {
    def sanitizedMessage = message.replace("\"", "\\\"").replace("\n", "\\n")
    sh """
        curl -X POST -H "Content-Type: application/json" \
        -d '{"content": "${sanitizedMessage}"}' \
        ${DISCORD_WEBHOOK_URL}
    """
}
