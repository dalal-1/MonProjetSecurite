pipeline {
    agent any
    environment {
        // Variables d'environnement adaptées à votre machine virtuelle
        APPLICATION_PATH = "/home/delaila/MonProjetSecurite"  // Chemin vers votre projet sur la machine virtuelle
        DEPLOYMENT_SCRIPT = "deploy.yml"  // Playbook Ansible pour déployer l'application
        TEST_SCRIPT = "run_tests.sh"  // Script de test (à adapter si nécessaire)
        SECURITY_CHECK_SCRIPT = "security_check.sh"  // Script de vérification de sécurité
        GITHUB_REPO = "https://github.com/your-repository.git"  // Remplacez par l'URL de votre dépôt GitHub
        BRANCH = "main"  // Branche du dépôt GitHub que vous souhaitez utiliser
        ANSIBLE_HOSTS = "/home/delaila/MonProjetSecurite/hosts.ini"  // Fichier d'inventaire Ansible
        JENKINS_HOME = "/var/jenkins_home"  // Emplacement de Jenkins sur Ubuntu (si nécessaire)
    }
    stages {
        stage('Checkout') {
            steps {
                // Cloner le dépôt GitHub sur la machine virtuelle
                git branch: "${BRANCH}", url: "${GITHUB_REPO}"
            }
        }
        
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    // Construction de l'application (ajustez le script ou la commande en fonction de vos besoins)
                    sh 'python3 -m venv venv' // Créer un environnement virtuel si nécessaire
                    sh '. venv/bin/activate'  // Activer l'environnement virtuel
                    sh 'pip install -r requirements.txt'  // Installer les dépendances
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the application...'
                    // Lancer le playbook Ansible pour déployer l'application
                    sh "ansible-playbook -i ${ANSIBLE_HOSTS} ${DEPLOYMENT_SCRIPT}"
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    // Exécuter les tests après le déploiement
                    sh "./${TEST_SCRIPT}"  // Exécution de votre script de tests (assurez-vous qu'il est exécutable)
                }
            }
        }
        
        stage('Security Check') {
            steps {
                script {
                    echo 'Running security checks...'
                    // Exécuter les vérifications de sécurité automatisées
                    sh "./${SECURITY_CHECK_SCRIPT}"  // Exécution du script de vérification de sécurité
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            // Nettoyage après exécution
            sh 'rm -rf venv'  // Exemple de nettoyage (à adapter selon vos besoins)
        }
        success {
            echo 'Deployment and testing completed successfully!'
        }
        failure {
            echo 'There was an error during the deployment process.'
        }
    }
}
