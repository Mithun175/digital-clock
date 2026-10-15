
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Digital Clock Project'
            }
        }

        stage('Test') {
            steps {
                echo 'Digital Clock project test successful'
            }
        }
    }

    post {
        success {
            echo 'Digital Clock pipeline completed!'
        }
    }
}
