pipeline {
    agent any

    environment {
        // Virtual environment name
        VENV_NAME = 'venv'
        HOST_NAME = 'localhost:8081'
        BASE_URL = '192.168.0.10:8081'
        SELENOID_URL = '192.168.0.10:4444/wd/hub'
        HOST_UID = sh(script: 'id -u', returnStdout: true).trim()
        HOST_GID = sh(script: 'id -g', returnStdout: true).trim()
        PATH="${env.PWD}/allure-2.24.1/bin:${env.PATH}"
        JAVA_HOME = '/opt/homebrew/opt/openjdk@21'
    }

    stages {
        stage('Checkout') {
            steps {
                    git (
                        url: 'https://github.com/TataRouS/Otus_graduation_project.git',
                        branch: 'graduate_branch'
                    )
                }
        }

        stage('Set up docker') {
            steps {
                script {
                    // Create virtual environment
                    sh '/usr/local/bin/docker build -t nata/pytest .'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Run pytest with Allure reporting
                    sh """
                        /usr/local/bin/docker run -e BASE_URL=$BASE_URL -e SELENOID_URL=$SELENOID_URL -v ./logs:/app/logs -v ./allure-results:/app/allure-results nata/pytest:latest || true
                    """
                }
            }
        }

        stage('Allure step') {
            steps {
                script {
                    sh """
                        allure generate allure-results -o allure-report --clean
                    """
                }
            }
        }
    }

    post {
        always {
            // Archive both results and report
            archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            archiveArtifacts artifacts: 'allure-report/**/*', allowEmptyArchive: true
            // Publish HTML report
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
            allure([results: [[path: 'allure-results']]]) // Replace 'allure-results' with your actual results directory
        }
    }
}