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
        self.level = {'Level':1, 'Current':0, 'Max':64} #Level 64 is enough to max out all stats
        self.hp = {'HP':10, 'Max':10}
        self.stats = {'Strength':1,      #attack dmg
                      'Agility':1,       #evasion
                      'Dexterity':1,     #health
                      'Intelligence':1,  #opens encounter options
                      'Will':1,          #resist mental attacks
                      'Charisma':1,      #opens npc options
                      'Luck':1,          #influence RNG and Charisma proc
                      'Max':10}          #maximum stat level
        self.stat_points = 0

    def level_up(self):
        """Runs process of selecting stat and allocating stat points to player stat
        """
        if self.stat_points == 0:
            return

        stat_names = ['Strength','Agility','Dexterity','Intelligence','Will','Charisma','Luck']
        maxed_stats = []
        for name in stat_names:
            if self.stats[name] == 10:
                write(name + " (MAX)")
                maxed_stats.append(name)
            else:
                write(name)

        time.sleep(1)
        while True:
            choice = str(input("Which stat to upgrade: "))
            if choice == "Return":
                break

            while choice not in stat_names or choice in maxed_stats:
                choice = str(input("Which stat to upgrade: "))
            
            amt = int(input(f"How many points to use ({self.stat_points})"))
            while amt > self.stat_points:
                amt = int(input(f"How many points to use ({self.stat_points})"))

            if (self.stats[choice] + amt) <= 10:
                self.stats[choice] += amt
                break
            else:
                write("Amount chosen is too high for stat \'{choice}\'")

    def lvl_check(self):
        """Checks if xp gained is enough to level up
        """
        if self.level['Current'] >= self.level['Max']:
            self.level['Level'] += 1
            self.level['Current'] -= self.level['Max']
            self.level['Max'] = self.level['Level'] * 100
            self.stat_points += 1

    def hp_check(self):
        """Checks if the use of a healing potion has over-healed the player
        """
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
    {keys[0]}: {vals[0]}   Points: {self.stat_points}
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
    print()
