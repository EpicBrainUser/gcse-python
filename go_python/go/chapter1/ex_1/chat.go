package main

import (
  "fmt"
  "math"
)

func main() {
    // 1. Basic arithmetic
    fmt.Println("Addition:", 5 + 3)           // 8
    fmt.Println("Subtraction:", 5 - 3)        // 2
    fmt.Println("Multiplication:", 5 * 3)     // 15

    // 2. Division (for integers)
    fmt.Println("Integer Division:", 5 / 2)   // 2 (truncated result)
    
    // 3. Division with floating-point result
    fmt.Println("Floating Division:", 5.0 / 2.0) // 2.5

    // 4. Modulo operation
    fmt.Println("Modulo:", 5 % 2)             // 1

    // 5. Exponentiation (using math.Pow for float64)
    fmt.Println("Exponentiation:", math.Pow(2, 3)) // 8.0 (2^3)

    // If you want an integer result from exponentiation, you can cast it
    result := int(math.Pow(2, 3))             // Cast result to int
    fmt.Println("Exponentiation as int:", result) // 8
}
