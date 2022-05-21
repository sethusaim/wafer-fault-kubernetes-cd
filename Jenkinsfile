pipeline {
  agent any

  stages {
    stage("Cloning Git") {
      steps {
        git branch: 'main', url: 'https://github.com/sethusaim/Wafer-Fault-Kubernetes-CD.git'
      }
    }

    stage('Update component') {
      environment {
        AWS_ACCOUNT_ID = credentials('AWS_ACCOUNT_ID')

        EC2_APP_IP = credentials("EC2_APP_IP")
      }

      steps {
        script {
          catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
              sh 'git config user.email sethusaim@gmail.com'

              sh 'git config user.name sethusaim'

              // sh 'export DOCKERTAG=${DOCKERTAG}'

              sh 'python3 update_component.py'

              sh 'git add .'

              sh 'git commit -m "Updated component for ${REPO_NAME} repository with build number as ${DOCKERTAG}"'

              sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/Wafer-Fault-Kubernetes-CD.git'

              if ($ {
                  REPO_NAME
                } == "wafer_application") {
                sshagent(credentials: ['ec2_ssh']) {
                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu ${EC2_APP_IP} python3 deploy_application.py'
                }
              } else {
                sh "echo pass"
              }
            }
          }
        }
      }
    }
  }
}