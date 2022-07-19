from os import system
import sys
import time


class Location:
    def __init__(self, name, coords, paths = ['N', 'E', 'S', 'W']) -> None:
        self.name: str = name
        self.coords: tuple = coords
        self.paths: list = paths


class Player:
    def __init__(self, name, race) -> None:
        self.name = name
        self.race = race
        self.level = {'Level':1, 'Current':0, 'Max':100}
        self.hp = {'HP':10, 'Max':10}
        self.stats = {'Strength':1, 
                      'Agility':1,
                      'Dexterity':1,
                      'Intelligence':1,
                      'Will':1,
                      'Charisma':1,
                      'Luck':1,
                      'Max':10}

    def level_up(self):
        choice = ' '
        keys, vals = [], []
        for key, val in self.stats.items():
            keys.append(key)
            vals.append(val)
        print(self.stats)
        while choice not in keys:
            try:
                choice = str(input('Which stat to upgrade: '))
                if self.stats[choice] != 10:
                    self.stats[choice] += 1
            except:
                print('Stat is maxed out')


    def lvl_check(self):
        if self.level['Current'] >= self.level['Max']:
            self.level['Level'] += 1
            self.level['Current'] -= self.level['Max']
            self.level['Max'] = self.level['Level'] * 100
            self.level_up()


    def hp_check(self):
        if self.hp['HP'] > self.hp['Max']:
            self.hp['HP'] = self.hp['Max']

    def __str__(self) -> str:
        keys, vals = [], []
        for key, val in self.stats.items():
            keys.append(key)
            vals.append(val)
        hud = f"""Name: {self.name}
Race: {self.race}
Level: {self.level['Level']} ({self.level['Current']}/{self.level['Max']})
HP: {self.hp['HP']}/{self.hp['Max']}
Stats:
    {keys[0]}: {vals[0]}
    {keys[1]}: {vals[1]}
    {keys[2]}: {vals[2]}
    {keys[3]}: {vals[3]}
    {keys[4]}: {vals[4]}
    {keys[5]}: {vals[5]}
    {keys[6]}: {vals[6]}"""
        return hud


def clear():
    """Clears terminal window of any written text.
    """
    system('cls')


def write(text):
    """Writes given text to screen formatted neatly.

    Args:
        text (string): A string to write to screen.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        x = 0.04
        if char in ',.!?':
            x = 0.3
        time.sleep(x)
