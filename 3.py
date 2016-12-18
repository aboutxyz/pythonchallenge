#coding:utf-8
import re
string = ''
a = re.compile("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
with open("3.txt",'r') as f:
    ip = a.findall(f.read())
    for i in ip:
        string += i[4]
    print string


