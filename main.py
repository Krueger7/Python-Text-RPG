from os import system, name
import sys
import time


def clear():
    system('cls')


def write(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        x = 0.04
        if char in ',.!?':
            x = 0.3
        time.sleep(x)


def main():
    write("Hello, World!")


if __name__ == "__main__":
    main()
