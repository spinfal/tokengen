import random
import string
import time as t
import os
from termcolor import colored as cl

tokenStart = ['MT', 'MD', 'NT']
speed = input(cl('fast or slow: ', 'white'))
if speed == 'fast':
  speed = 0.1
elif speed == 'slow':
  speed = 0.4
else:
  print(cl(speed, 'red') + ' is not a valid option')
  t.sleep(2)
  os.system('python3 main.py')

f = open('randomTokens.txt', 'w+')
f.write('there is a low chance of finding a working token, but it is never zero.\n\n')
f.close()

while True:
  sel = random.randint(0,2)
  def get_random_string(length):
      random_list = []
      for i in range(length):
          random_list.append(random.choice (string.ascii_letters + string.digits))
      return ''.join(random_list)

  token = tokenStart[sel] + get_random_string(1) + get_random_string(1) + get_random_string(20) + '.' + random.choice(string.ascii_letters).upper() + get_random_string(5) + '.' + get_random_string(27)
  print(cl(token + '\n', 'cyan'))
  f = open('randomTokens.txt', 'a+')
  f.write(token + '\n')
  f.close()
  t.sleep(speed)