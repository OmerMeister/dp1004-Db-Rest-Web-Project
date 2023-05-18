pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/OmerMeister/GitExercise.git'
      }
    }

    stage('Run Python Script') {
      steps {
                // Run the Python script
                bat 'python main.py'
      }
    }
  }
}
