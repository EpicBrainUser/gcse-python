package main

import "fmt"

func addAndPrintParameters(x int, y int, z int){
  result:= x+y+z
  fmt.Printf("The sum of %d %d, and %d is %d", x, y, z, result)
}

func main(){
  addAndPrintParameters(15, 13, 5)
}
