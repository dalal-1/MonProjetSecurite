pipeline {
    agent any

    tools {
        // Déclare les outils nécessaires ici (si tu en utilises)
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupère le code depuis le repository
                checkout scm
            }
        }
        
        stage('Dependency Check') {
            steps {
                script {
                    // Lancer l'analyse avec Dependency-Check sur le répertoire courant
                    dependencyCheck additionalArguments: '', 
                                   scanPath: '.', 
                                   dataDirectory: 'dependency-check-data', 
                                   failBuildOnCVSS: '7', 
                                   analysisType: 'SCA', 
                                   format: 'HTML', 
                                   outputDirectory: 'dependency-check-report'
                }
            }
        }

        // Ajouter ici d'autres étapes si nécessaire, comme tests ou déploiement
    }

    post {
        always {
            // Actions à effectuer après chaque build (si besoin)
        }
    }
}
