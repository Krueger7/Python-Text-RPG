from tools import *


def main():
    name = input('Name: ')
    race = ''
    while race not in ['Human', 'Elf', 'Dwarf']:
        race = input('Race (Human, Elf, Dwarf): ')
    playerIG = Player(name, race)
    print(playerIG)

    region = Map()
    print(region)


if __name__ == "__main__":
    main()
