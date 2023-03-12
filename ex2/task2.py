import os
import os.path
from pprint import pprint
import json

adr = input()

# C:\Users\small\Downloads\papka1

d = dict()

def tree(adr):
    
    if(os.path.isfile(adr)):
            file = {"name": os.path.basename(adr), "size": os.stat(adr).st_size, "type": "normal"}            
            return (file)
    
    cld = os.scandir(adr)               
    dir = {"type": "dir", "name": os.path.basename(adr), "children": [tree(i) for i in cld]}    
    return(dir)
        

# d["children"] = tree(adr)
# pprint(d,width = 1)

d = {"children": tree(adr)}
pprint(d,width = 1)

with open('C:\dev\Python\POSU\ex2\\fileSys.json', 'w') as f:
    json.dump(d, f)

with open('C:\dev\Python\POSU\ex2\\fileSys.json') as f:
    print(f.read())