package main

import "fmt"

func getStudentName() string {
  var studentName string
  fmt.Printf("Please enter your name: ")
  fmt.Scan(&studentName)
  return studentName
}

func getTeacherName() string {
  var teacherName string
  fmt.Printf("\nPlease enter your Computer Science teacher's name: ")
  fmt.Scan(&teacherName)
  return teacherName
}

func getMarks() float32 {
  var marks1 float32
  var marks2 float32
  var marks3 float32
  fmt.Printf("\nWhat were your last three marks for computer science?\n")
  fmt.Scan(&marks1)
  fmt.Scan(&marks2)
  fmt.Scan(&marks3)
  var average float32 = (marks1 + marks2 + marks3)/3
  return average
}

func teacherComment(studentName string, teacherName string, average float32){
  if average >=8 {
    fmt.Printf("\n Well done, %s, %s, is very pleased with your effort.\n", studentName, teacherName)
  } else if average >=6 {
    fmt.Printf("\n A good effort, %s, but %s thinks you should check your work carefully.\n", studentName, teacherName)
  } else if average <5 {
    fmt.Printf("\n%s this is poor. %s has asked you to try harder.\n", studentName, teacherName)
  } else {
    fmt.Printf("\n 🧢")
  }
}

func main(){
  studentName := getStudentName()
  teacherName := getTeacherName()
  average := getMarks()
  teacherComment(studentName, teacherName, average)
}
