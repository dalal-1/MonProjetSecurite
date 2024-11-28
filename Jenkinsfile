pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Nmap') {
  steps {
    bat 'echo %PATH%'
    bat 'nmap --version'
  }
}


        
    }
}
