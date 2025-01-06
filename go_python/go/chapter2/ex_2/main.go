package main

import (
  "fmt"
  "math"
)

func main(){
  const π float64 = 3.142
  fmt.Println("π is 3.142")
  var radius float64 = 6.7
  var radiusSquared = math.Pow(radius, 2)
  var area float64 = radiusSquared * π
  fmt.Println("The area is the radius squared * π")
  fmt.Printf("Which in this case is %v squared multiplied by %v.\n", radius, π)
  fmt.Printf("so the answer is %v\n", area)
}
