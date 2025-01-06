name = input("whats your name?\n")
subscribers = int(input("how many subs?\n"))


#def manual_str_formatting(name,subscribers):
if subscribers > 100000:
    print(f"Wow {name}! you have {subscribers} subscribers")
else:
    print(f"Lol {name} that's not many subs")
