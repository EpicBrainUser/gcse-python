package main

import (
  "fmt"
)

func main(){
  var amount int
  fmt.Println("We only dispense 10s and 20s. Input what cash you would like: ")
  fmt.Scan(&amount)
  if amount > 0 && amount % 10 == 0 {
    fmt.Printf("ok, your total is %d\n", amount)
  } else{
    fmt.Println("invalid amount")
  }
}
