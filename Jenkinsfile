pipeline {
    agent any

    environment {
        GIT_URL = 'https://github.com/dalal-1/MonProjetSecurite.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    // Checkout du dépôt depuis la branche 'main'
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${env.BRANCH_NAME}"]],
                        userRemoteConfigs: [[url: env.GIT_URL]]
                    ])
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Commande pour installer les dépendances, si applicable
                    echo "Installing dependencies..."
                    // Exemple : sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Start Application') {
            steps {
                script {
                    // Démarrer l'application ou d'autres processus
                    echo "Starting the application..."
                    // Exemple : sh 'python app.py'
                }
            }
        }

        stage('Start ZAP for Security Scan') {
            steps {
                script {
                    // Démarrer OWASP ZAP pour le scan de sécurité
                    echo "Starting ZAP for security scan..."
                    // Exemple : sh 'zap.sh -daemon -config api.disablekey=true'
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    // Lancer un scan Nmap
                    echo "Running Nmap scan..."
                    // Exemple : sh 'nmap -sS localhost'
                }
            }
        }

        stage('Run Nikto Scan') {
            steps {
                script {
                    // Lancer un scan Nikto
                    echo "Running Nikto scan..."
                    // Exemple : sh 'nikto -h http://localhost'
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    // Effectuer le scan de sécurité avec ZAP
                    echo "Running ZAP scan..."
                    // Exemple : sh 'zap-cli active-scan --url http://localhost'
                }
            }
        }

        stage('Stop ZAP') {
            steps {
                script {
                    // Arrêter ZAP après le scan
                    echo "Stopping ZAP..."
                    // Exemple : sh 'zap-cli shutdown'
                }
            }
        }

        stage('Stop Application') {
            steps {
                script {
                    // Arrêter l'application ou autres services
                    echo "Stopping application..."
                    // Exemple : sh 'kill $(ps aux | grep app.py | awk '{print $1}')'
                }
            }
        }

        stage('Generate Reports') {
            steps {
                script {
                    // Générer des rapports après les scans
                    echo "Generating reports..."
                    // Exemple : sh 'python generate_reports.py'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs() // Nettoie l'espace de travail après l'exécution
        }
    }
}
