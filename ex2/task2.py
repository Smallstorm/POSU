import os
from pprint import pprint
import stat

adr = input()

cld = os.listdir(adr)
print(cld,'\n')
print(os.path.abspath("task2.py"))

# C:\Users\small\Downloads\papka1

d = dict()

def tree(adr):
    if(os.isfile(adr)):
        file = {"name": os.path.basename(adr), "size": os.stat(adr).st_size, "type": "normal"}
        print("file", file["name"])

d["children"] = list()

# file1 = {"name": os.path.basename(adr), "size": os.stat(adr).st_size, "type": "normal"}
# file2 = {"name": os.path.basename(adr), "size": os.stat(adr).st_size, "type": "normal"}

# d["children"] = [file1,file2]

# pprint(d)