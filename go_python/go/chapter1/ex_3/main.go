package main

import (
  "fmt"
)

func main(){
  var minutes int
  fmt.Println("Enter time in minutes: ")
  fmt.Scan(&minutes)

  hours := minutes / 60
  remainingMinutes := minutes % 60

  fmt.Printf("The time is %d hours and %d minutes.\n", hours, remainingMinutes)
}
