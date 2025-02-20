package main 

import "fmt"

func milesToKilometers() float32 {
  var input float32
  fmt.Println("Enter the miles you wish to convert to kilometers: ")
  fmt.Scan(&input)
  km := input * 1.61
  fmt.Printf("\nThat's %v km. \n", km)
  return km
}

func main() {
  milesToKilometers()
}
