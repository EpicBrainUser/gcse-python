package main

import "fmt"

func getValidNumber(){
  for {
    var number int
    fmt.Printf("Enter a valid number between 1 and 12\n")
    fmt.Scan(&number)
    if number < 1 || number > 13 {
      fmt.Printf("Number not in range, please re-enter the number")
      return number
      break

    } else {
      fmt.Printf("Number in correct range, proceed. \n")
      fmt.Scan(&number)
    }
  }
}

func main(){

}
