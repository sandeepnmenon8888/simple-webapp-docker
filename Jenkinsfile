pipeline {
    agent any

    environment {
        OCP_URL = "https://api.crc.testing:6443"        // Change if your cluster uses a different API URL
        OCP_PROJECT = "dockerapp"
        APP_NAME = "hello-world"
        REGISTRY_IMAGE = "image-registry.openshift-image-registry.svc:5000/dockerapp/hello-world:latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/sandeepnmenon8888/simple-webapp-docker.git'
            }
        }

        stage('Build Image Locally') {
            steps {
                sh 'docker build -t $APP_NAME:latest .'
                sh 'docker save $APP_NAME:latest -o image.tar'
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
                sh 'oc start-build $APP_NAME --from-archive=image.tar --wait --follow'
            }
        }

        stage('Update Deployment Image') {
            steps {
                sh 'oc set image deployment/$APP_NAME $APP_NAME=$REGISTRY_IMAGE'
            }
        }
    }
}
