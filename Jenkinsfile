pipeline {
    agent any

    stages {
        stage('Check source') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '**']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'github-ssh-key', url: 'git@github.com:mmblsp/webcount.git']]
                ])
            }
        }
        stage('Git Pull') {
            steps {
                git branch: '', credentialsId: 'github-ssh-key', url: 'git@github.com:mmblsp/webcount.git'
            }
        }
        stage('Test') {
            steps {
                sh 'tox'
            }
        }
    }
}