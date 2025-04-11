package main

import (
	"fmt"
)

func getValidNumber() int {
	var number int
	fmt.Printf("Enter a valid number between 1 and 12\n")
	fmt.Scan(&number)
	if number < 1 || number > 12 {
		fmt.Printf("Number not in range, please re-enter the number")
		return getValidNumber()
	} else {
		fmt.Printf("Number in correct range, proceed. \n")
		return number
	}
}

func printTimesTable(number int) {
	fmt.Printf("You entered: %v\nThe Times Tables for that number are:\n", number)
	for i := 1; i < 13; i++ {
		result := number * i
		if i < 10 {
			fmt.Printf(" %v x %v = %v\n", i, number, result)
		} else {
			fmt.Printf("%v x %v = %v\n", i, number, result)
		}
	}
}

func main() {
	number := getValidNumber()
	printTimesTable(number)
	fmt.Println("And for exercise two: ")
	sum, err := GetAndAddNumbers()
	if err != nil {
		fmt.Println("Error: ", err)
	} else {
		fmt.Println("Sum of added numbers: ", sum)
	}
}
