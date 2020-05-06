#!/usr/bin/env python3

mylist = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
Answer = input('What Marvel Character would you line to know about? Flash, Batman or Superman')
Answer2 = input('What statistic would you like to know about? Speed, Intelligence or strenght?')
print ( mylist[Answer][Answer2] )
