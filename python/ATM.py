print("We only dispense 10s and 20s. Input what cash you would like: ")

cash = int(input())

if cash%10==0:
    print("That is fine.")
    print('You are withdrawing £', cash + '.')
  
else:
    print("We cannot dispense that amount.")


