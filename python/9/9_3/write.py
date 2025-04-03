#!/usr/bin/python3

# def write(content, file):
#     with open(file, "w") as f:
#         f.write(f"{content}")


def write(names, file):
    with open(file, 'w') as file:
        for name in names:
            file.write(f"{name}\n")



