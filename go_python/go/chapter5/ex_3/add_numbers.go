package main

import (
	// "errors"
	"fmt"
)

func GetAndAddNumbers() (float32, error) {
	var sum, input float32
	// var err error
	fmt.Printf("This program stores numbers until you enter 0, then prints the sum of the previously added numbers.\nPlease start entering your numbers below\n")
	for {
		fmt.Print("> ")
		_, err := fmt.Scan(&input)
		if err != nil {
			return sum, fmt.Errorf("invalid input: must enter a number")
		}

		if input == 0 {
			return sum, nil
		}

		sum += input

		fmt.Printf("Current sum: %.2f\n", sum)

	}

}
