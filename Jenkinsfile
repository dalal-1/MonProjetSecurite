pipeline {
    agent any

    environment {
        ZAP_PORT = 8081
        APP_PORT = 5000
        APP_URL = "http://localhost:${APP_PORT}"
        NMAP_RESULTS = "nmap_results.xml"
        NIKTO_RESULTS = "nikto_results.html"
    }

    stages {
        stage('Clone Project') {
            steps {
                script {
                    // Clone the Git repository
                    git 'https://github.com/dalal-1/MonProjetSecurite.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Start Application') {
            steps {
                script {
                    // Start the Flask application in the background
                    echo 'Starting Flask application...'
                    sh 'source venv/bin/activate && nohup python3 app.py &'
                }
            }
        }

        stage('Start ZAP for Security Scan') {
            steps {
                script {
                    // Start ZAP in daemon mode on the specified port
                    echo 'Starting ZAP...'
                    sh "zap.sh -daemon -port ${ZAP_PORT} -config spider.maxChildren=5"
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    // Wait for the application to start
                    echo 'Waiting for application to start...'
                    sleep(time: 30, unit: 'SECONDS')

                    // Perform Nmap scan to find open ports and vulnerabilities
                    echo 'Running Nmap scan...'
                    sh "nmap -sV -oX ${NMAP_RESULTS} ${APP_URL}"
                }
            }
        }

        stage('Run Nikto Scan') {
            steps {
                script {
                    // Perform Nikto scan to check for web vulnerabilities
                    echo 'Running Nikto scan...'
                    sh "nikto -h ${APP_URL} -o ${NIKTO_RESULTS} -Format htm"
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    // Run a quick scan using zap-cli or ZAP API
                    echo 'Running ZAP scan...'
                    sh "zap-cli quick-scan --self-contained ${APP_URL}"
                }
            }
        }

        stage('Stop ZAP') {
            steps {
                script {
                    // Stop ZAP after the scan
                    echo 'Stopping ZAP...'
                    sh 'zap-cli shutdown'
                }
            }
        }

        stage('Stop Application') {
            steps {
                script {
                    // Stop the Flask application
                    echo 'Stopping Flask application...'
                    sh 'pkill -f "python3 app.py"'
                }
            }
        }

        stage('Generate Reports') {
            steps {
                script {
                    // Archive the results from Nmap, Nikto, and ZAP
                    echo 'Archiving scan results...'
                    archiveArtifacts artifacts: '${NMAP_RESULTS}, ${NIKTO_RESULTS}, zap_report.html', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace after every run
            echo 'Cleaning up...'
            cleanWs()
        }
    }
}
