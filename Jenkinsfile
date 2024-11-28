pipeline {
    agent any
    
    environment {
        // Définir l'environnement avec les clés et URL
        DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/1311140096829030401/nGEZ9k6p6JD8fH7ijln8t8Isftrd77PO385KvNadsXM_xjw9k8Wtj13kSkla1jF2YzrV'
        CODACY_API_TOKEN = '01db00b69eac4393a4f5b8f081702953'
    }
    
    stages {
        stage('Cloner le dépôt Git') {
            steps {
                // Cloner le dépôt Git en spécifiant la branche 'main'
                git branch: 'main', url: 'https://github.com/dalal-1/MonProjetSecurite.git'
            }
        }
        
        stage('Exécution des tests de sécurité') {
            steps {
                // Exécuter Bandit pour analyser la sécurité de l'application Python
                sh 'python -m bandit -r app.py -f html -o bandit-report.html'
                
                // Exécuter SonarQube pour analyser le code
                sh 'mvn sonar:sonar -Dsonar.projectKey=MonProjetSecurite -Dsonar.host.url=http://localhost:9000 -Dsonar.login=your-sonar-token'

                // Exécuter OWASP ZAP pour tester la sécurité de l'application
                sh 'zap-cli quick-scan --self-contained --spider --active-scan http://localhost:5000'

                // Envoi des rapports à Discord
                script {
                    def message = "Tests de sécurité terminés. Les résultats sont disponibles dans les rapports."
                    sh "curl -X POST -H 'Content-Type: application/json' -d '{\"content\": \"${message}\"}' ${DISCORD_WEBHOOK}"
                }
            }
        }
        
        stage('Déployer l’application avec Ansible') {
            steps {
                // Se connecter via SSH à la machine virtuelle et exécuter le playbook Ansible
                sshagent(['delaila']) {
                    sh 'ansible-playbook -i /home/delaila/MonProjetSecurite/inventory /home/delaila/MonProjetSecurite/deploy.yml'
                }
            }
        }
        
        stage('Codacy Verification') {
            steps {
                script {
                    // Exécuter Codacy pour la vérification de la qualité du code
                    def response = httpRequest(
                        url: "https://api.codacy.com/2.0/project/$CODACY_API_TOKEN/verify",
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON'
                    )
                    echo "Codacy Response: ${response}"
                }
            }
        }
        
        stage('Notification Discord') {
            steps {
                script {
                    // Envoyer une notification à Discord après le déploiement
                    def message = "Déploiement terminé avec succès pour l'application sécurisée."
                    sh "curl -X POST -H 'Content-Type: application/json' -d '{\"content\": \"${message}\"}' ${DISCORD_WEBHOOK}"
                }
            }
        }
    }
    
    post {
        success {
            echo "Le pipeline s'est exécuté avec succès."
        }
        failure {
            echo "Le pipeline a échoué."
        }
    }
}
