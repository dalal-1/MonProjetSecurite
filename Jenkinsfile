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
                    sendDiscordNotification("🛠️ **Étape 2 : Scan Nmap Terminé** 🕵️‍♂️\nLe scan des ports a été effectué. Voici un résumé des résultats :\n\n```txt\n$(cat /var/lib/jenkins/nmap_scan_results.txt)```.\n\nLes détails complets sont enregistrés dans un fichier texte. [Consultez-le ici](file:///var/lib/jenkins/nmap_scan_results.txt).")
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
                    sendDiscordNotification("🚨 **Étape 3 : Scan ZAP Terminée** ✅\nLe scan de sécurité a été effectué avec succès. Un rapport détaillé est disponible.\n\n🔑 **Rapport de sécurité ZAP** : [Cliquez ici pour le rapport HTML](file:///var/lib/jenkins/zap_reports/zap_report.html).")
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    echo "Toutes les étapes du pipeline sont terminées."
                    sendDiscordNotification("🎉 **Pipeline Terminée avec succès !** 🎉\nToutes les étapes ont été exécutées sans erreur et les rapports ont été générés. Vérifiez les résultats des scans Nmap et ZAP ci-dessus.")
                }
            }
        }
    }

    post {
        always {
            sendDiscordNotification("🔔 **Exécution du Pipeline : ${currentBuild.result}** - ${env.BUILD_URL}\nConsultez le lien vers les résultats du build ci-dessus.")
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
