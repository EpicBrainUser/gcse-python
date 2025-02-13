#!/usr/local/bin/python3
import subprocess
import os


def append(content, file, mode):
    with open(file, mode) as f:
        f.write(f"{content}")
        f.write("Content appended to the file.")


