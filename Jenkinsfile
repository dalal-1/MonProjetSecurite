pipeline {
    agent any
    stages {
        stage('ZAP Security Scan') {
            steps {
                sshagent(['delaila-ssh-key']) {
                    sh '''
                    ssh delaila@192.168.1.101 "zaproxy -daemon -host 192.168.1.101 -port 9090"
                    '''
                }
            }
        }
        stage('Run Security Scan') {
            steps {
                // Ajoutez ici des étapes pour interagir avec l'API ZAP pour démarrer le scan
                sh '''
                curl http://192.168.1.101:9090/JSON/ascan/action/scan
                '''
            }
        }
    }
}
