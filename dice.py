import random

print("What is your name?")
name = input()
print("Hello, %s!" % name)

print("Rolling dice...")

num1 = random.randint(1, 6)
print("Die 1:",num1)
num2 = random.randint(1, 6)
print("Die 2:",num2)

sum = num1 + num2
print("Total value:",sum)

if(sum > 7): print("You won")
else: print("You lost")
