pipeline {
    agent any

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
    }
}
