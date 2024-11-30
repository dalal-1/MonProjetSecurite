pipeline {
    agent any

    environment {
        // Variables d'environnement nécessaires
        NMAP_SCAN_TARGET = 'localhost'
        ZAP_URL = 'http://localhost:5000'
        BANDIT_REPORT = 'bandit_report.txt'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Vérification du code source..."
                checkout scm
            }
        }

        stage('Run Bandit Security Scan') {
            steps {
                script {
                    try {
                        echo "Lancement du scan de sécurité Bandit..."
                        sh 'bandit -r ./ -o $BANDIT_REPORT'
                        echo "Scan Bandit terminé. Rapport généré : $BANDIT_REPORT"
                    } catch (Exception e) {
                        echo "Des vulnérabilités ont été détectées par Bandit, mais le pipeline continue."
                    }
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    try {
                        echo "Lancement du scan Nmap..."
                        // Vérification si l'utilisateur a les privilèges root avant d'exécuter Nmap
                        if (sh(script: 'id -u', returnStdout: true).trim() == '0') {
                            sh "nmap -T4 -sS -p 80,443 $NMAP_SCAN_TARGET"
                        } else {
                            echo "Nmap nécessite des privilèges root. Exécutez avec 'sudo' pour un scan complet."
                        }
                    } catch (Exception e) {
                        echo "Le scan Nmap a échoué ou nécessite des privilèges root. Le pipeline continue."
                    }
                }
            }
        }

        stage('Run OWASP ZAP Scan') {
            steps {
                script {
                    try {
                        echo "Lancement du scan avec OWASP ZAP..."
                        // Vérifie si ZAP est installé et l'exécute
                        if (sh(script: 'command -v zaproxy', returnStatus: true) == 0) {
                            sh "zaproxy -cmd -quickurl $ZAP_URL -quickout zap_report.html"
                            echo "Scan ZAP terminé. Rapport généré : zap_report.html"
                        } else {
                            echo "OWASP ZAP n'est pas installé ou non accessible. Le scan ZAP n'a pas été effectué."
                        }
                    } catch (Exception e) {
                        echo "Le scan ZAP a échoué. Le pipeline continue."
                    }
                }
            }
        }

        stage('Post Actions') {
            steps {
                echo "Exécution des actions de post-traitement..."
                // Exemple d'action après le scan
                sh './post_actions.sh'
            }
        }
    }

    post {
        always {
            echo "Pipeline terminé. Rapport de vulnérabilités disponible."
        }
        success {
            echo "Le pipeline s'est terminé avec succès malgré les éventuelles vulnérabilités détectées."
        }
        failure {
            echo "Le pipeline a échoué, mais certaines étapes ont pu se terminer correctement."
        }
    }
}
