pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Ajoute des étapes de build si nécessaire
            }
        }

        stage('Vulnerability Scan') {
            steps {
                echo 'Running Nmap Vulnerability Scan on HTTP service...'

                // Commande Nmap pour scanner le service HTTP de ton application Flask
                script {
                    def target = '127.0.0.1'  // Cible l'IP locale
                    def port = '5000'         // Port utilisé par Flask (5000 par défaut)
                    
                    // Utilisation de Nmap pour détecter les vulnérabilités HTTP sur le port 5000
                    sh "nmap -p ${port} --script=http-vuln* --open --reason ${target}"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Ajoute ici les étapes de déploiement
            }
        }
    }
}
