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
      }

      steps {
        script {
          catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
              sh 'git config user.email sethusaim@gmail.com'

              sh 'git config user.name sethusaim'

              sh 'python3 update_component.py'

              sh 'git add .'

              sh 'git commit -m "Updated component for ${REPO_NAME} repository with build number as ${DOCKERTAG}"'

              sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/Wafer-Fault-Kubernetes-CD.git'

              if (${REPO_NAME} == "wafer_application") {
                sshagent(credentials: ['ec2_ssh']) 
                {
                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu 52.6.101.26 wget https://raw.githubusercontent.com/sethusaim/Wafer-Fault-Kubernetes-CD/main/update_component.py'

                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu 52.6.101.26 python3 deploy_application.py'
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