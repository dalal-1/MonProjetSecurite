pipeline {
    agent any

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Test Sécurité avec OWASP ZAP') {
            steps {
                echo "This is where the security tests with OWASP ZAP would run."
                // If you want to invoke a simple script or command for OWASP ZAP, 
                // make sure it runs on Windows, or you can use a Docker container.
            }
        }

        stage('Envoyer Notification Discord') {
            steps {
                echo "Notification sent to Discord"
                // You can use `curl` to send a Discord notification here.
                // Ensure that `curl` is available on your Windows agent.
            }
        }
    }

    post {
        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
