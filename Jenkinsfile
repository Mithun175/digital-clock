
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy Website') {
            steps {
                bat '''
                if not exist C:\\DigitalClockSite mkdir C:\\DigitalClockSite
                xcopy /E /I /Y "%WORKSPACE%\\index.html" "C:\\DigitalClockSite\\"
                xcopy /E /I /Y "%WORKSPACE%\\style.css" "C:\\DigitalClockSite\\"
                '''
            }
        }

        stage('Start Local Website') {
            steps {
                bat '''
                powershell -NoProfile -ExecutionPolicy Bypass -Command "$listener = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue; if (-not $listener) { Start-Process -FilePath 'python' -ArgumentList '-m http.server 8000 --directory C:\\DigitalClockSite' -WindowStyle Hidden }"
                '''
            }
        }
    }
}
