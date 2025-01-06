package main

import "fmt"

func main(){
  var n int = 0
  for i:=0; i<100000000; i++{
    n +=1
    fmt.Printf("n is %v\n", n)
  }
  } 
