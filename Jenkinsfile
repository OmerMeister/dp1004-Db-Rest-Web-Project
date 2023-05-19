pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/OmerMeister/Db_Rest_Web-Project.git'
      }
    }
    stage('install prerequisits') {
      steps {
                bat 'python -m pip install requests'
      }
    }
                stage('Run clean_environment.py') {
      steps {
                bat 'python clean_environment.py'
                echo "squence ended"
      }
    }    
    //closing braces
  }
}
