## Chapter 2

2. ```py
   π=3.142
   radius = 6.7
   areaOfCircle=π*radius**2
   ```

3. ```python
   forname = input('please type your forename >>')
   surname = input('please type your surname >>')
   age = input('please type your age >>')
   print('your name is', forname surname, 'and you are', age, 'years old')
   ```
   
   ## Chapter 3

### Type errors

These are when you try to use a string like a integer, for example you don't
use ```int(input('hi'))```

### Quotes

Which one should I use?
Using single quotation marks means that you need to use escape characters in the string if you also want to use characters like a backslash, apostrophe or double quotation marks.
Using double quotation marks means that you do not need to use escape characters.
Using triple quotation marks means that text can span several lines. These are used for “docstrings” and multiple-line comments.

### Escape character

'```\```' followed by 't' (tab), 'n' (new line) and qutoes to allow for useage in
other quotes

### Strings

Strings are immutable, meaning that once you've done one you can't change it

Putting variables in a print statement can be done using a '+' or a ','.

#### String formatting

```python
  1 string = "Computer Science is fun!"
  2
  3 print(string.upper())
  4 print(string[3:9])
  5 print(string[8:])
  6 print(string[:9])
~
~
```

```
COMPUTER SCIENCE IS FUN!
puter 
 Science is fun!
Computer 
```

To make a certain string have upper/lower case, or only print certain parts of it, you can specify it when printing, as shown above

##### Exercise 2

**f strings**

you can also connect variables in print statements with fstrings, as shown below

```python
#Average of two numbers

a = int(input("what is your first number \n"))
b = int(input("what is your second number \n"))

print(f"The average of your two numbers is {(a+b)/2}")
```

And you can print multiple lines with a single print statement, as shown below 

```python
print("There are two papers for computer science:\n\t1. Computer Systems \n\t2. Computational thinking, algorithms and programming")
```

Escape characters are used for this, namely ```\n``` and ```\t``` 

### Using ord() and chr()

This is a very simple python program that shifts the inputted letters by the desihred key

```python
toBeEncrypted = input("Please type your message to be encrypted here \n >>>")
encryptedMessage = ''
key = int(input("Please type the key you wish to use here \n >>>"))

for each in toBeEncrypted:
    newLetter = ord(each) + key
    encryptedMessage += chr (newLetter)

print(encryptedMessage)
```

### OCR string operations questions

1. RebEl

#### 3.3

The variale Bob is assigned a value.

```python
message = "fred1234"
```



```
print(message.length)
```

gives 

```
8
```

```
print(message.upper)
```

gives 

```
FRED1234
```

```
print(message.left(4)
```

gives 

```
fred
```

and finally 

``` 
print(int(message.right(4))*2)
```



gives 



```
2468
```



## Chapter 4. Functions & Procedures
