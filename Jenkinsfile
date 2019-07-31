pipeline {
  agent any
  triggers {
    pollSCM('H/15 * * * ')
  }
  stages {
    stage('Build Container') {
      agent {
        label "Pi_3"
      }
      steps {
        sh "docker build -t zflux ."
      }
    }
    stage('Tag Container') {
      agent {
        label "Pi_3"
      }
      steps {
        sh "docker tag zflux fx8350:5000/zflux:latest"
        sh "docker tag zflux leonhess/zflux:latest"
      }
    }
    stage('Push to Registries') {
      parallel {
        stage('Push to local Registry') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker push fx8350:5000/zflux:latest"
          }
        }
        stage('Push to DockerHub') {
          agent {
            label "Pi_3"
          }
          steps {
            withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
              sh "docker push leonhess/zflux:latest"
            }
          }
        }
      }
    }
    stage('Cleanup') {
      agent {
        label "Pi_3"
      }
      steps {
        sh "docker rmi fx8350:5000/zflux:latest"
        sh "docker rmi leonhess/zflux:latest"
      }
    }
    stage('Deploy to swarm') {
      agent {
        label "master"
      }
      steps {
        ansiblePlaybook(
          playbook: 'deploy.yml',
          credentialsId: '78c069cd-77c4-4c91-89cc-7805f3c9cfe2'
          )
        }
      }
    }
  }
