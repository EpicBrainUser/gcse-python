import random

starters = ["sh", "ash", "ksh"]
mains = ["bash", "dash", "zsh"]
deserts = ["fish", "tcsh", "csh"]

starter_choice = random.randint(0,len(starters)-1)
mains_choice = random.randint(0,len(mains)-1)
deserts_choice = random.randint(0,len(deserts)-1)

print(f"Your random choice is {starters[starter_choice]}, {mains[starter_choice]} and {deserts[deserts_choice]}")
