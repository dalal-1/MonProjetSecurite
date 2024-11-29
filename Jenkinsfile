pipeline {
    agent any

    environment {
        // Ajoutez vos variables d'environnement ici
        ZAP_HOST = "192.168.1.101"       // IP de la machine virtuelle Delaila
        ZAP_PORT = "9090"                // Port par défaut pour OWASP ZAP
        SSH_CREDENTIALS_ID = "delaila-ssh-key" // ID des credentials SSH dans Jenkins
    }

    stages {
        stage('Initialize ZAP') {
            steps {
                sshagent([env.SSH_CREDENTIALS_ID]) {
                    sh '''
                    ssh delaila@${ZAP_HOST} "zaproxy -daemon -host ${ZAP_HOST} -port ${ZAP_PORT}"
                    '''
                }
            }
        }

        stage('Run Security Scan') {
            steps {
                echo 'Running ZAP Security Scan...'
                // Exemple de commande pour interagir avec ZAP via son API
                sh '''
                curl "http://${ZAP_HOST}:${ZAP_PORT}/JSON/ascan/action/scan/?url=http://example.com&recurse=true&inScopeOnly=true"
                '''
            }
        }

        stage('Retrieve Scan Report') {
            steps {
                echo 'Retrieving ZAP Scan Report...'
                // Exemple pour exporter un rapport en HTML
                sh '''
                curl "http://${ZAP_HOST}:${ZAP_PORT}/OTHER/core/other/htmlreport/" -o zap_report.html
                '''
                archiveArtifacts artifacts: 'zap_report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up ZAP...'
            // Fermez OWASP ZAP après le scan
            sh '''
            ssh delaila@${ZAP_HOST} "pkill -f zaproxy"
            '''
        }
    }
}
