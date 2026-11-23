pipeline {
    agent any

    stages {
        stage('Build Application') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }
    }
}
