pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials-id'
        REPO_URL = 'https://github.com/your-username/habit-tracker.git'
        IMAGE_NAME = 'sachin8927/habit-tracker'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml' // Path to Docker Compose file
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
                script {
                    // Placeholder for running tests. Adjust as needed.
                    echo 'Running tests...'
                    
                    // Example test command. Replace or add your actual test commands here.
                    sh '''
                    echo "No tests defined, skipping..."
                    '''
                }
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
                script {
                    // Stop and remove existing containers
                    echo 'Stopping and removing existing containers...'
                    sh '''
                    docker-compose -f ${DOCKER_COMPOSE_FILE} down
                    '''

                    // Start new containers with the updated image
                    echo 'Starting new containers...'
                    sh '''
                    docker-compose -f ${DOCKER_COMPOSE_FILE} up -d
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
