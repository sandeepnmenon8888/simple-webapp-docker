pipeline {
    agent any

    environment {
        OCP_URL = "https://host.docker.internal:6443"
        OCP_PROJECT = "dockerapp"
        APP_NAME = "hello-world"
        REGISTRY_IMAGE = "image-registry.openshift-image-registry.svc:5000/dockerapp/hello-world:latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sandeepnmenon8888/simple-webapp-docker.git'
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

        stage('Start OpenShift Build') {
            steps {
                sh 'oc start-build $APP_NAME --wait --follow'
            }
        }

        stage('Apply Deployment (with volume)') {
            steps {
                sh 'oc apply -f deployment.yaml -n $OCP_PROJECT'
            }
        }

        stage('Restart Deployment') {
            steps {
                sh 'oc rollout restart deployment/$APP_NAME -n $OCP_PROJECT'
            }
        }
    }

    post {
        success {
            echo "✅ Jenkins pipeline completed successfully."
        }
        failure {
            echo "❌ Jenkins pipeline failed."
        }
    }
}
