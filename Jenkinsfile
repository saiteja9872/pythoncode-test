node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarqube9090';
    withSonarQubeEnv() {
      sh "python3 --version"
    }
  }
}
