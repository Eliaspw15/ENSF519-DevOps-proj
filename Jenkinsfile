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
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                sh '''
                    set -e

                    python3 -m venv .venv
                    .venv/bin/pip install selenium

                    # Serve the production build
                    python3 -m http.server 4173 \
                        --bind 127.0.0.1 \
                        --directory dist \
                        > /tmp/selenium-server.log 2>&1 &

                    SERVER_PID=$!
                    trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

                    # Verify server responds before testing
                    for i in $(seq 1 20); do
                        if curl -fsS http://127.0.0.1:4173/ >/dev/null; then
                            break
                        fi
                        sleep 1
                    done

                    curl -f http://127.0.0.1:4173/

                    TEST_URL=http://127.0.0.1:4173 \
                        .venv/bin/python tests/test_website.py
                '''
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
