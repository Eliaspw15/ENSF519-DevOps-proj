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

                    # Create Python environment
                    python3 -m venv .venv
                    .venv/bin/python -m pip install selenium 

                    # Serve the production build
                    python3 -m http.server 4173 \
                        --bind 127.0.0.1 \
                        --directory dist \
                        > /tmp/selenium-server.log 2>&1 &

                    SERVER_PID=$!
                    trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

                    # Wait for website to become available
                    for i in $(seq 1 20); do
                        if curl -fsS http://127.0.0.1:4173/ >/dev/null; then
                            break
                        fi
                        sleep 1
                    done

                    # Verify website is responding
                    curl -fsS http://127.0.0.1:4173/ >/dev/null

                    # Run all tests and generate JUnit report
                    export TEST_URL=http://127.0.0.1:4173

                    for file in tests/test_*.py; do
                        echo "================================="
                        echo "Running $file"
                        echo "================================="

                        .venv/bin/python -u "$file" || exit 1
                    done
                '''
            }
        }
    }
}
