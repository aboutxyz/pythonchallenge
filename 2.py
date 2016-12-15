import os,sys

a = ''
with open('ocr.txt', 'r') as f:
    for line in f.read():
        if line.isalpha():
            a += line
print a