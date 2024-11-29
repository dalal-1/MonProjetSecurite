pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Initialize ZAP') {
            steps {
                // Utilisation de l'agent SSH pour se connecter à la machine distante
                sshagent(credentials: ['delaila']) {
                    script {
                        // Commande pour démarrer ZAP en mode daemon sur l'hôte distant
                        sh 'ssh user@192.168.1.101 "zaproxy -daemon -host 192.168.1.101 -port 9090"'
                    }
                }
            }
        }
        stage('Check ZAP Status') {
            steps {
                sshagent(credentials: ['delaila']) {
                    script {
                        // Vérifier si ZAP est bien en fonctionnement sur la machine distante
                        sh 'ssh user@192.168.1.101 "ps aux | grep zaproxy"'
                    }
                }
            }
        }
    }
}
