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
                // Placeholder for test steps
                echo 'Running tests...'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials-id', url: 'https://index.docker.io/v1/']) {
                    sh 'docker push sachin8927/habit-tracker'
                }
            }
        }


        stage('Deploy') {
            steps {
                // Placeholder for deploy steps
                echo 'Deploying application...'
                // Use Docker Compose or other tools to deploy
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
