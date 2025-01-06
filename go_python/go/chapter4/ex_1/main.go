package main

import "fmt"

func addAndPrint() {
  x := 17
  y := 22
  result := x + y
  fmt.Printf("The sum of %d and %d is %d\n", x, y, result)
}

func main (){
  addAndPrint()
}
