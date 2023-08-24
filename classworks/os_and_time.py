import os
import time
from datetime import timedelta, datetime

a=time.time()

print(time.altzone)
print(time.asctime())

# time.sleep(2)

b=time.time()

print(b-a)
print(time.strftime('%A, %D %B %Y %I:%M %p'))

curr_month=datetime.now().month

print(curr_month-2)
print(os.name)

# print(os.environ)

print(os.access('pycache',os.W_OK))

# os.chdir('C://')

# print(os.listdir())

# os.rmdir('test')

# os.remove('pycache/abramyan_functions.cpython-311.pyc')

os.rename('test.py','another_file.py')