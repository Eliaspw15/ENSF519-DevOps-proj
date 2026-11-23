pipeline {
    agent any

    stages {
        stage('Build Application') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }

        stage('Selenium Tests') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install selenium

                    npm run preview -- --host 127.0.0.1 &
                    SERVER_PID=$!

                    trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

                    sleep 5
                    .venv/bin/python tests/test_website_jenkins.py
                '''
            }
        }
    }
}
