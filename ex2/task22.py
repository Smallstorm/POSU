import json
import os

dict = {}
adr = input()

a = os.listdir(adr)
# b = os.path.exists(adr)
c = os.path.isfile(adr)

print('child' , a)

def tree(node):       
    if(not node.find('.') == -1):  # if file
        print('file --> ', node,'\n') 
        # dict["children"] = dict.get("children", []) + [{"name" : os.path.basename(child_adr), "size" : os.stat(child_adr).st_size,"type" : "normal" }]                                     
        return
    b = os.listdir(adr + '\\' + node)
    print('children of ',node,'are\n',b,'\n')
    list(map(tree, b))
    return(dict)
for i in a:
    print('loop after for ' ,i)
    tree(i)        



# C:\Users\small\Pictures