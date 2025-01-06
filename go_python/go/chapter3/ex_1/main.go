package main

import (
  "fmt"
  "strings"
)

func main() {
  myString := "This is a string"
  length := len(myString)
  fmt.Printf("The length of the string is : %d\n", length)
  upperCaseString := strings.ToUpper(myString)
  fmt.Printf("The first string in upper case is: %s\n", upperCaseString)
  substring := myString[3:9]
  substringToEnd := myString[3:]
  substringFromStart := myString[:9]
  fmt.Printf("The substring from index 3 to 9 is: %s\n", substring)
  fmt.Printf("The substring from index 3 to end is: %s\n", substringToEnd)
  fmt.Printf("The substring from index start to 9 is: %s\n", substringFromStart)


  var num1, num2 float64
  fmt.Println("This program averages out two numbers.\nPlease enter your first number:")
  fmt.Scan(&num1)
  fmt.Println("Now please enter your second number: ")
  fmt.Scan(&num2)
  var average float64 = (num1/num2)/2
  fmt.Printf("The average of your two numbers is %v\n", average)

  fmt.Printf("There are two papers for GCSE Computer Science:\n\t1. Computer Systems\n\t2. Computational Thinking, Algorithms and Programming\n")
}
