pipeline {
    agent any
    stages {
        stage('PowerShell Test') {
            steps {
                // Afficher les variables d'environnement
                bat 'echo %PATH%' 
                bat 'cmd /c echo Hello from CMD'
                bat 'powershell -Command "Write-Host \'Hello from PowerShell!\'"'
            }
        }
    }
}
