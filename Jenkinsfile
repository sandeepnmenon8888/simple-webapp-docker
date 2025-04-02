pipeline {
    agent any

    environment {
        OCP_URL = "https://api.crc.testing:6443"
        OCP_PROJECT = "dockerapp"
        APP_NAME = "hello-world"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/YOUR_USERNAME/simple-webapp-docker.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'podman build -t $APP_NAME:latest .'
                sh 'podman save $APP_NAME:latest -o image.tar'
            }
        }

        stage('Login to OpenShift') {
            steps {
                withCredentials([string(credentialsId: 'ocp-token', variable: 'OCP_TOKEN')]) {
                    sh '''
                        oc login $OCP_URL --token=$OCP_TOKEN --insecure-skip-tls-verify
                        oc project $OCP_PROJECT
                    '''
                }
            }
        }

        stage('Push Image to OpenShift') {
            steps {
                sh 'oc start-build $APP_NAME --from-archive=image.tar --follow'
            }
        }

        stage('Restart Deployment') {
            steps {
                sh 'oc rollout restart dc/$APP_NAME'
            }
        }
    }
}
