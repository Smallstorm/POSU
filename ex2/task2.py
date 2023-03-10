import json
import os

adr = input()

# a = os.listdir(adr)
b = os.path.exists(adr)
c = os.path.isfile(adr)

# for i in a:
    # print(os.path.isfile(i))
    # print(i,'-->',os.path.isfile(i))

dir = []
file = []
dict = {}

c = os.listdir(adr)
# print(c)

def dick(c):
    next = False
    print('\n start with c == ', c)
    j = 0
    
    while(j < len(c)):
        while(not next):        
            print('\nc[j] = ',c[j])

            child_adr = adr + '\\' + c[j]        
            # if(os.path.isdir(child_adr)):
            if(not c[j].find('.') == -1):
                print(j)       
                dict["children"] = dict.get("children", []) + [{"name" : os.path.basename(child_adr), "size" : os.stat(child_adr).st_size,"type" : "normal" }]                              
                
            else:                
                c = os.listdir(child_adr)                
                dick(c)       
            next = True
            j += 1
            break
            # dick(c)
    # print('j in the end',j)
    # c.pop()    
    return(dict)        
# dick(c)

c = os.listdir(adr)
print('c = ',c)
dick(c)
# del c[0:2]
# # print('b = ',b)
# print('new c = ',c)
# dick(c)    
# if(os.path.isfile(adr)):    
#     print('file')   
#     dict["name"] = os.path.basename(adr)     
#     dict["size"] = os.stat(adr).st_size
#     dict["type"] = "normal"     



# def is_dir(adr):
#     # global adr
#     print('\ncurrent address = ',adr)
#     if(not os.path.isfile(adr)):
#         c = os.listdir(adr)
#         print('\nc = ',c)
#         # for j in c:  # ходим по содержанию папки                
#         j = 0
#         while(j < len(c)):    
#             print(j)
#             child_adr = adr + '\\' + c[j]
#             print('child adr',child_adr)
#             if(not os.path.isfile(child_adr)):    
#                 c = os.listdir(child_adr)                
#                 print('dir \t child c == ', c)
#                 adr = child_adr    
#                 is_dir(adr)
                 
#             else:     
                              
#                 dict["name"] = os.path.basename(child_adr)     
#                 dict["size"] = os.stat(child_adr).st_size
#                 dict["type"] = "normal"  
#                 print('file')
                
#                 # print('adr after all ',adr)
#             j += 1

#             r = child_adr[::-1]        
#             e = r.find('\\')
#             print('r =',r,'\t','e = ',e)
#             back = r[e+1:]
#             adr = back[::-1]
#             print('back = ',back,'adr = ',adr)
                
# is_dir(adr)

# dict2 = {
#   "name": "Ford",
#   "type": "Mustang",
#   "size": 1964,
#   "children": [  {
#             "name": "Ford",
#             "type": "Mustang",
#             "size": 1964
#               }] 
# }   

for key, value in dict.items():
    print(key,':',value)
# # C:\Users\small\Downloads
# # C:\Users\small\Pictures\malish1.jpg 