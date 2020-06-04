from time import sleep
from random import randint
import sys

print('sleeping...')
sleep(5)

print('hello world')
print('receiving:', sys.argv)
print(randint(1, 6))
# save dataframe to csv
csv = 'data.csv'
print('csv is', csv)
