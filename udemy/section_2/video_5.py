import pandas as pd, numpy, matplotlib

name = 'Bob'
if name == 'Alice':
  print('Hi, Alice')
print('Done')  

password = 'python'
if password == 'swordfish':
  print('Access granted.')
else:
  print('Wrong password.')

print()
name = 'Bob'
age = 3000
if name == 'Alice':
  print('Hi, Alice')
elif age < 12:
  print('You are not Alice, kiddo.')
elif age > 2000:
  print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
  print('You are not Alice, grannie.') 

print()
print('Enter a name.')
name = input()
if name != '':
  print('Thank you for entering a name.')
else:
  print('You did not enter a name.')  
