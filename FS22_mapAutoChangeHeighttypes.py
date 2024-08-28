#!/usr/bin/env python
__author__ =  "limone81"
__version__ = "0.1"
__status__ = "dev"

### imports
from bs4 import BeautifulSoup
import os


### set path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

### main
file = open('map.i3d', 'r')
soup = BeautifulSoup(file, 'xml')

# get position
a = soup.find('DetailLayer', numDensityMapChannels='12')
print(f'raw_value: {a}')

# change attributes
a['numDensityMapChannels'] =  '14'
a['compressionChannels'] = '7'
a['combinedValuesChannels'] = '0 7 0'
a['heightFirstChannel'] = '7'
a['heightNumChannels'] = '7'

# check attributes
print('\n')
print(f'changed_value: {a}')
b = soup.find('DetailLayer', numDensityMapChannels='14')
print(f'new_search : {b}')

file.close()