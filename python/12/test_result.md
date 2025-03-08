# Test result for the Inventory Management game from chapter 8 (ex 5)

Here I test one of my older python projects, namely the role play game from chapter 8.

| Test number | Test description | Data input                                                         | Expected outcome                         | Actual outcome                           | Improvements |
| ----------- | ---------------- | ------------------------------------------------------------------ | ---------------------------------------- | ---------------------------------------- | ------------ |
| 1           | Normal           | Follow the menu structure of the game, and entering the valid data | The program does what is says it will do | The program does what is says it will do | None.        |

```
                Game Menu

                A - Enter Name
                B - Play Game
                C - Quit
Please enter your choice: A
That is a valid choice
What is your name?
 >EpicBrainUser
Hello EpicBrainUser, it's good to see you
                Game Menu

                A - Enter Name
                B - Play Game
                C - Quit
Please enter your choice: B
That is a valid choice
Game is starting...
                Actual Game Menu


            A - Print Inventory Items
            B - Add Item To Inventory
            C - Remove Item From Inventory
            D - View selected item
            E - Get item from inventory
            F - Return selected item to inventory
            G - Quit
Please enter your choice: G
That is a valid choice



sorry to see you go.
                Game Menu

                A - Enter Name
                B - Play Game
                C - Quit
Please enter your choice: C
That is a valid choice
Thank you for playing
```

| Test number | Test description | Data input                                                                          | Expected outcome                                                | Actual outcome                                                                     | Improvements |
| ----------- | ---------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| 2           | Boundery         | Insert name of item as with many special characters, such as quotes and backslashes | The list escapes these characters and prints the list as normal | The program does exactly as it's supposed to, ans shown below, and prints the list | None.        |

```
Game is starting...
        Actual Game Menu


            A - Print Inventory Items
            B - Add Item To Inventory
            C - Remove Item From Inventory
            D - View selected item
            E - Get item from inventory
            F - Return selected item to inventory
            G - Quit
Please enter your choice: b
That is a valid choice



Enter the item name to add: asd;fkasd;fkajsd' '''asdf \
asd;fkasd;fkajsd' '''asdf \ has been added to your inventory.
        Actual Game Menu


            A - Print Inventory Items
            B - Add Item To Inventory
            C - Remove Item From Inventory
            D - View selected item
            E - Get item from inventory
            F - Return selected item to inventory
            G - Quit
Please enter your choice: a
That is a valid choice



The current inventory is:

1. asd;fkasd;fkajsd' '''asdf \
```

| Test number | Test description | Data input                                                                                   | Expected outcome                                                                                                        | Actual outcome                | Improvements |
| ----------- | ---------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------ |
| 3           | Invalid          | Selecting letters that aren't options, such as 'g' for the first menu, or 'm' for the second | The program returns a message telling the user their input was invalid, and prompts the user to enter the result again. | Just as expected, shown below | None.        |

```
        Game Menu

        A - Enter Name
        B - Play Game
        C - Quit
Please enter your choice: g
That is not a valid choice
Please enter your choice: \
That is not a valid choice
Please enter your choice: '
That is not a valid choice
Please enter your choice: @
That is not a valid choice
Please enter your choice: "
That is not a valid choice
Please enter your choice: b
That is a valid choice
Game is starting...
        Actual Game Menu


            A - Print Inventory Items
            B - Add Item To Inventory
            C - Remove Item From Inventory
            D - View selected item
            E - Get item from inventory
            F - Return selected item to inventory
            G - Quit
Please enter your choice: m
That is not a valid choice



Please enter your choice: "
That is not a valid choice



Please enter your choice: '
That is not a valid choice



Please enter your choice: k
That is not a valid choice



Please enter your choice: g
That is a valid choice



sorry to see you go.
        Game Menu

        A - Enter Name
        B - Play Game
        C - Quit
Please enter your choice: c
That is a valid choice
Thank you for playing
```

| Test number | Test description | Data input | Expected outcome | Actual outcome | Improvements |
| ----------- | ---------------- | ---------- | ---------------- | -------------- | ------------ |
| 4           | Erroneous        |            |                  |                |              |
