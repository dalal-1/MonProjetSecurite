pipeline {
    agent any

    environment {
        // Définir les variables d'environnement nécessaires, comme l'ID de l'agent SSH
        ZAP_HOST = '192.168.1.101'
        ZAP_PORT = '9090'
    }

    stages {
        // Étape de checkout du code depuis Git
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        // Étape d'initialisation de ZAP
        stage('Initialize ZAP') {
            steps {
                script {
                    // S'assurer que ZAP est lancé en mode daemon sur la machine distante
                    echo 'Démarrage de ZAP en mode daemon'
                    sshagent(['delaila']) {
                        sh '''
                        ssh delaila@192.168.1.101 "zaproxy -daemon -host 192.168.1.101 -port 9090"
                        '''
                    }
                }
            }
        }

        // Étape de scan de sécurité
        stage('Run Security Scan') {
            steps {
                script {
                    echo 'Lancement du scan de sécurité avec ZAP'
                    // Ici, vous pouvez ajouter des commandes pour effectuer le scan via l'API ZAP
                    sshagent(['delaila']) {
                        sh '''
                        # Commande pour lancer un scan via ZAP, exemple avec l'API ou un script personnalisé
                        ssh delaila@192.168.1.101 "zaproxy -cmd -host 192.168.1.101 -port 9090 -scan"
                        '''
                    }
                }
            }
        }

        // Étape pour récupérer le rapport du scan
        stage('Retrieve Scan Report') {
            steps {
                script {
                    echo 'Récupération du rapport du scan de sécurité'
                    // Commande pour récupérer les résultats du scan de sécurité depuis ZAP, par exemple avec l'API
                    sshagent(['delaila']) {
                        sh '''
                        scp delaila@192.168.1.101:/home/delaila/.ZAP/report.html ./report.html
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Le pipeline a réussi, le scan de sécurité est terminé et les rapports sont récupérés.'
        }
        failure {
            echo 'Le pipeline a échoué. Vérifiez les étapes du scan de sécurité.'
        }
    }
}
