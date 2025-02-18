package main

import "fmt"


var number int

func recursive(){
	fmt.Println("Enter a number between 1 and 20")
	fmt.Scan(&number)
	if number <1 || number >20 {
		fmt.Println("Number out of range, please try again")
		recursive()
	} else{
		fmt.Println("Number in range, continue")
	}
}

func switchBlock(){
	yay := true
	for yay{
		fmt.Println("Enter a number between 1 and 20")
		fmt.Scan(&number)

		switch {
		case number > 0 && number <= 20:
			fmt.Println("Number is between 1 and 20")
			yay = false
		default:
			fmt.Println("Number not in range")
		}


/* 		switch{
		case number > 0 && number <= 20:
			fmt.Println("Number in range, continue")
			yay = false
		default:
			fmt.Println("Number out of range, please try again")
		}
 */	
	}
}

func ifBlock(){
	yay:= true
	for yay{
		fmt.Println("Enter a number between 1 and 20")
		fmt.Scan(&number)
		if number > 0 && number <=20{
			fmt.Println("Number in range, continue")
			yay = false
		} else{
			fmt.Println("Number out of range, please try again")
		}
	}
}

func main(){
	var selection int
	yay := true
	for yay{
		fmt.Printf("\nPlease choose which version to run by entering the corresponding number, we have: \n1. Recursion\n2. For loops (If statement for validation)\n3. For loops (Switch block)\n4. Quit\n")
		fmt.Scan(&selection)
		switch selection{
		case 1:
			recursive()
		case 2:
			ifBlock()
		case 3:
			switchBlock()
		case 4:
			yay = false
		default:
			fmt.Print("Not an option, try again\n")
		}
	}
	
}