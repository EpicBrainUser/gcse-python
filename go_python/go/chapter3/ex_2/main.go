package main

import (
  "fmt"
)

func ceasarCipher(plainText string, shift int) string {
  shifted := []rune(plainText)

  for i, char := range shifted {

    if char >= 'A' && char <= 'Z' {
      shifted[i] = 'A' + (char-'A'+rune(shift))%26
    } else if char >= 'a' && char <= 'z' {
        shifted[i] = 'a' + (char-'a'+rune(shift))%26 
    }
  }
  return string(shifted)
}

func main(){
  plainText := "This is plaintext"
  shift := 7

  encrypted := ceasarCipher(plainText, shift)
  fmt.Println("Original:", plainText)
  fmt.Println("Encrypted:", encrypted)

}
