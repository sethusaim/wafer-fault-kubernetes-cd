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
            }

            if (${REPO_NAME} == "wafer_application") {
                sshagent (credentials: ['ec2_ssh']) {
                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu 52.6.101.26 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 347460842118.dkr.ecr.us-east-1.amazonaws.com'

                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu 52.6.101.26 wget https://raw.githubusercontent.com/sethusaim/Wafer-Fault-Kubernetes-CD/main/deploy_app.sh'

                  sh 'ssh -o StrictHostKeyChecking=no -l ubuntu 52.6.101.26 bash deploy_app.sh'
                }
              } 
              else {
                sh "echo pass"
              }
            }
          }
        }
      }
    }
  }