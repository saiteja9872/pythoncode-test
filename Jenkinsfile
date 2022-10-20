node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner 2.8';
    withSonarQubeEnv() {
      sh "python3 --version"
    }
  }
}
