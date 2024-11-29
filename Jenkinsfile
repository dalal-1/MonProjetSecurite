pipeline {
    agent any
    stages {
        stage('Initialize ZAP') {
            steps {
                sshagent(credentials: ['cdabd150-c297-45cf-80c5-2c5307c16d9c']) { // Utilise l'ID unique de l'identifiant SSH
                    // Exécute la commande SSH sur le serveur distant
                    sh 'ssh user@192.168.1.101 "ton-commande"'
                }
            }
        }
    }
}
