import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

name = 'Carol'
age = 3000
if name == 'Alice':
  print('Hi, Alice.')
elif age < 12:
  print('You are not Alice, kiddo.')
elif age > 2000:
  print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
  print('You are not Alice, grannie.')
  