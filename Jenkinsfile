pipeline {
    agent any
    stages {
        stage('PowerShell Test') {
            steps {
                script {
                    // Exécuter un script PowerShell directement dans Jenkins
                    bat 'powershell.exe -Command "Write-Host \'Hello from PowerShell!\'"'
                }
            }
        }
    }
}
