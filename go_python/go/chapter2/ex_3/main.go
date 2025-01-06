package main

import "fmt"

func main(){
  var forename string
  var surname string
  var age int
  fmt.Println("What is your forename?")
  fmt.Scan(&forename)
  fmt.Println("What is your surname?")
  fmt.Scan(&surname)
  fmt.Println("What is your age?")
  fmt.Scan(&age)
  fmt.Printf("You are %v %v and are %v years old\n", forename, surname, age)
}
