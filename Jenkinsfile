pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/dalal-1/MonProjetSecurite.git'
        BRANCH = 'main'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Récupération du code depuis le dépôt Git
                git url: "${GIT_REPO}", branch: "${BRANCH}"
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Installe les dépendances, ajuste en fonction des besoins
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Security Scan') {
            steps {
                script {
                    // Exécuter le scan de sécurité (ajuste la commande en fonction de ton outil)
                    sh 'zap-baseline.py -t http://localhost:5000'
                }
            }
        }
    }

    post {
        failure {
            // Si le pipeline échoue, une notification Discord peut être ajoutée ici
            echo 'Le pipeline a échoué.'
        }
    }
}
