import os
import sys

directory = r"C:\Users\Tush-R D'situation\AppData\Local\Programs\Python\Python37-32"

line_count = {}

for filename in os.listdir(directory):
    _,ext = os.path.splitext(filename)
    if ext not in line_count:
        line_count[ext] = 0
    for line in open(os.path.join(directory, filename), encoding="utf8"):
        line_count[ext] += 1

for ext, line in line_count.items():
    print('Extension {} had {} lines'.format(ext, count))
    
