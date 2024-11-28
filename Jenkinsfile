pipeline {
    agent any

    environment {
        // Add necessary environment variables, like paths to executables
        PATH = "C:\\Program Files\\Git\\bin;C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Job_2_Pipeline\\nmap;C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts" // Adjust paths if needed
    }

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    try {
                        echo "Checking out the repository..."
                        checkout scm
                    } catch (Exception e) {
                        error "Failed to checkout repository: ${e.getMessage()}"
                    }
                }
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
                    try {
                        echo "Checking Nmap version..."
                        bat 'nmap --version'
                    } catch (Exception e) {
                        error "Nmap version check failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Install Bandit') {
            steps {
                script {
                    try {
                        echo "Installing Bandit for Python security analysis..."
                        bat 'python -m pip install --upgrade pip'
                        bat 'pip install bandit'
                    } catch (Exception e) {
                        error "Bandit installation failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Run Bandit Analysis') {
            steps {
                script {
                    try {
                        echo "Running Bandit analysis on Python code..."
                        bat 'bandit -r . -f json -o bandit-report.json'
                    } catch (Exception e) {
                        error "Bandit analysis failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Vulnerability Scan') {
            steps {
                script {
                    try {
                        echo "Starting vulnerability scan..."
                        // Add your vulnerability scan logic here
                        // Ensure that the necessary tools are installed and paths are set
                    } catch (Exception e) {
                        error "Vulnerability scan failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    try {
                        echo "Performing post actions..."
                        // Your post actions like sending reports, notifications, etc.
                    } catch (Exception e) {
                        error "Post actions failed: ${e.getMessage()}"
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed. Please check the logs for more details."
        }
    }
}
