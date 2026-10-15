
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Mithun175/digital-clock.git'
            }
        }

        stage('Run Digital Clock') {
            steps {
                bat 'python --version'
                bat 'python -u digital_clock.py'
            }
        }
    }
}
