node {
  stage('SCM') {
    checkout scm
  }
  stage("SonarQube analysis") {
        steps {
            script {
                def scannerHome = tool 'SonarQube Scanner';
                withSonarQubeEnv('SonarQube Server') {
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }
    }
}
