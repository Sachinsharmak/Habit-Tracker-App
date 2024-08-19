pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials-id'
        REPO_URL = 'https://github.com/Sachinsharmak/Habit-Tracker-App.git'
        IMAGE_NAME = 'sachin8927/habit-tracker'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Test') {
            steps {
                // Placeholder for test steps. Add unit tests or other checks here.
                echo 'Running tests...'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application. Here, you might use Docker Compose or other deployment tools.
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
