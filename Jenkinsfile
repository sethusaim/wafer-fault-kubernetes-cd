pipeline {
  agent any

  stages {
    stage("Cloning Git") {
      steps {
        git branch: 'main', url: 'https://github.com/sethusaim/Wafer-Fault-Kubernetes-CD.git'
      }
    }

    stage('Update Kubeflow component') {
      environment {
        AWS_ACCOUNT_ID = credentials('AWS_ACCOUNT_ID')

      }

      steps {
        script {

          catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
              sh 'git config user.email sethusaim@gmail.com'

              sh 'git config user.name sethusaim'

              sh 'sed -i "s+${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/{REPO_NAME}:.*+${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/{REPO_NAME}:${BUILD_NUMBER}+g" components/{COMP_FILE}'

              sh 'git add .'

              sh 'git commit -m Updated kubeflow component for ${REPO_NAME} repository with build number as ${BUILD_NUMBER}'

              sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/Wafer-Fault-Kubernetes-CD.git HEAD:main'

            }
          }
        }
      }
    }
  }
}