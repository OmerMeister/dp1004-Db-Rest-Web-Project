pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/OmerMeister/GitExercise.git'
      }
    }

    stage('Run rest_app.py') {
      steps {
                bat 'start/min python rest_app.py'
      }
    }
        stage('Run web_app.py') {
      steps {
                bat 'start/min python web_app.py'
      }
    }
            stage('Run backend_testing.py') {
      steps {
                bat 'python backend_testing.py'
      }
    }
            stage('Run frontend_testing.py') {
      steps {
                bat 'python frontend_testing.py'
      }
    }
            stage('Run combined_testing.py') {
      steps {
                bat 'python combined_testing.py'
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
