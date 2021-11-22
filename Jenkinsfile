pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/pratyushranjan2/Jenkins-1.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "python Prog1.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "python Test1.py"
                sh "python Test2.py"
            }
        }
    } 
}
