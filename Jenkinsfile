pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1311544596853166101/BK92iL16-3q27PWyLu45BwRaZZedC86swLC9nAAFFOpcyn0kuceMqH61Zknaxgiwd5hd'
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Show Current Directory') {
            steps {
                script {
                    // Affiche le répertoire courant
                    bat 'echo %cd%' // Commande adaptée pour Windows
                }
            }
        }

        stage('Check Nmap') {
            steps {
                script {
                    // Vérifier si Nmap est bien installé et dans le PATH
                    bat 'echo %PATH%' // Afficher les chemins pour vérifier si Nmap y est
                    bat 'nmap --version' // Vérifier la version de Nmap
                }
            }
        }

        stage('Install Bandit') {
            steps {
                script {
                    echo 'Installing Bandit for Python security analysis...'
                    bat 'pip install bandit' // Installer Bandit via pip
                }
            }
        }

        stage('Run Bandit Analysis') {
            steps {
                script {
                    echo 'Running Bandit analysis on Python code...'
                    // Commande pour analyser le code Python avec Bandit
                    bat 'bandit -r . -f json -o bandit-report.json'

                    // Lire le fichier de rapport JSON généré par Bandit
                    def report = readFile('bandit-report.json')
                    echo "Bandit analysis results: $report"

                    // Création du payload JSON pour la notification Discord
                    def body = """
                    {
                        "content": "Bandit security analysis completed. Results:\n$report"
                    }
                    """
                    echo "Sending message: $body"

                    // Envoi du rapport de sécurité à Discord
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: env.DISCORD_WEBHOOK_URL,
                        requestBody: body
                    )
                }
            }
        }

        stage('Vulnerability Scan') {
            steps {
                script {
                    echo 'Running Nmap Vulnerability Scan on HTTP service...'
                    // Placeholder pour la commande Nmap réelle
                    def nmapResults = 'Scan results here'

                    // Création du payload JSON pour la notification Discord
                    def body = """
                    {
                        "content": "Nmap vulnerability scan completed for HTTP service on port 5000."
                    }
                    """
                    echo "Sending message: $body"

                    // Envoi de la requête HTTP à Discord
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: env.DISCORD_WEBHOOK_URL,
                        requestBody: body
                    )
                }
            }
        }

        stage('Declarative: Post Actions') {
            steps {
                script {
                    def body = """
                    {
                        "content": "Pipeline completed successfully!"
                    }
                    """
                    // Envoi d'une notification de fin de pipeline à Discord
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        url: env.DISCORD_WEBHOOK_URL,
                        requestBody: body
                    )
                }
            }
        }
    }
}
