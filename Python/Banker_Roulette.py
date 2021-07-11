'''Banker Roulette- Who will pay the bill?
'''
import random

names=input("Give me everybody's names, separated by a comma. ").split()
bill=random.choice(names)
print(f"{bill} have to pay the bill")