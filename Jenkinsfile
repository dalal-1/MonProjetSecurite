pipeline {
    agent any

    environment {
        // Define environment variables (adjust the paths if needed)
        PATH = "${env.PATH};C:/Program Files (x86)/Nmap;C:/Users/ASUS/AppData/Local/Programs/Python/Python313/;C:/Users/ASUS/AppData/Local/Programs/Python/Python313/Scripts/"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Current Directory') {
            steps {
                script {
                    echo "Current workspace: ${env.WORKSPACE}"
                }
            }
        }

        stage('Check Nmap') {
            steps {
                script {
                    echo "Checking Nmap version..."
                    bat 'nmap --version'
                }
            }
        }

        stage('Install Bandit') {
            steps {
                script {
                    echo "Installing Bandit for Python security analysis..."
                    // Ensure pip is updated first
                    bat 'python -m pip install --upgrade pip'
                    bat 'pip install bandit'
                }
            }
        }

        stage('Run Bandit Analysis') {
            steps {
                script {
                    echo "Running Bandit analysis on Python code..."
                    // Run Bandit and output the result in JSON format
                    bat 'bandit -r . -f json -o bandit-report.json'
                    // Ensure the report file is generated
                    script {
                        def report = readFile('bandit-report.json')
                        echo "Bandit Report Content: ${report}"
                    }
                }
            }
        }

        stage('Vulnerability Scan') {
            when {
                expression {
                    return fileExists('bandit-report.json')
                }
            }
            steps {
                script {
                    echo "Running vulnerability scan..."
                    // Add your vulnerability scan logic here (Nmap, OWASP ZAP, etc.)
                    bat 'nmap -sV -T4 -oN nmap-report.txt localhost'
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    echo "Performing post-actions..."
                    // Add any necessary cleanup or notifications
                    // For example, notify if the report was generated
                    echo "Build completed with Bandit report: bandit-report.json"
                }
            }
        }
    }

    post {
        always {
            // Always clean up after the build
            cleanWs()
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs for more details."
        }
    }
}
