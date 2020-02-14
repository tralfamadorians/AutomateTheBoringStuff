import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':
    continue
  print('Hello, Joe. What is the password? (It is a fish.)')
  password = input()
  if password == 'swordfish':
    break
print('Access granted.')  

print()
print()
print()

name = ''
while not name:
  print('Enter your name:')
  name = input()
print('How many guests will you have?')
numofGuests = int(input())
if numofGuests:
  print('Be sure to have enough room for all your guests.')
done = 'Done'  
print(done)   