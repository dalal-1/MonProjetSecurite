pipeline {
    agent any

    environment {
        // Configuration de l'agent SSH (remplacez 'delaila' par le nom correct de votre clé SSH)
        SSH_KEY = 'delaila' 
        ZAP_HOST = '192.168.1.101'
        ZAP_PORT = '9090'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Initialize ZAP') {
            steps {
                script {
                    echo 'Démarrage de ZAP en mode daemon'
                    // Lancer ZAP en mode daemon
                    sshagent([SSH_KEY]) {
                        sh 'ssh delaila@${ZAP_HOST} "zaproxy -daemon -host ${ZAP_HOST} -port ${ZAP_PORT}"'
                    }
                }
            }
        }

        stage('Check ZAP Status') {
            steps {
                script {
                    echo 'Vérification de l\'état de ZAP'
                    // Vérifier si ZAP est bien en cours d\'exécution sur le port 9090
                    sshagent([SSH_KEY]) {
                        sh 'ssh delaila@${ZAP_HOST} "curl -s http://${ZAP_HOST}:${ZAP_PORT}"'
                    }
                }
            }
        }

        stage('Run Security Scan') {
            steps {
                script {
                    echo 'Lancer le scan de sécurité'
                    // Vous pouvez ajouter ici le lancement de votre scan avec ZAP
                    sshagent([SSH_KEY]) {
                        // Exemple de commande pour lancer un scan de sécurité avec ZAP
                        sh 'ssh delaila@${ZAP_HOST} "zaproxy -cmd -quickurl http://example.com -scanners 1001"'
                    }
                }
            }
        }

        stage('Retrieve Scan Report') {
            steps {
                script {
                    echo 'Récupérer le rapport de scan'
                    // Exemple pour récupérer le rapport de scan généré
                    sshagent([SSH_KEY]) {
                        sh 'scp delaila@${ZAP_HOST}:/path/to/report.html ./'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Le pipeline a réussi.'
        }
        failure {
            echo 'Le pipeline a échoué. Vérifiez les étapes du scan de sécurité.'
            // Ajouter une capture d'erreur si nécessaire
        }
    }
}
