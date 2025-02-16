pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-creds')
        DOCKER_IMAGE = 'luther443/my-nginx-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/megabyte77/docker_app_ci.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-creds') {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sh(script: """
                    docker stop my-app || true
                    docker rm my-app || true
                    docker run -d --name my-app -p 80:80 ${DOCKER_IMAGE}:${env.BUILD_ID}
                    """)
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