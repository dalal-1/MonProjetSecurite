pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/dalal-1/MonProjetSecurite.git'  
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Security Tests') {
            steps {
                script {
                    sh 'bandit -r .'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory deploy-flask-app.yml'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed.'
        }
    }
}
