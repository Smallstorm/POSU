import json
from pprint import pprint

with open('input.jsonc', 'r') as f:
          text = json.load(f)

pprint(text)

num_to_remove = list()
i = 0
j = 0
while(i < len(text)):    

    if (isinstance(text[i],list)):  #list edit
        num_to_remove.clear()  
        for j in range(len(text[i])):
            if(j % 2 == 0 and text[i][j] != None):                
                num_to_remove.append(text[i][j])  #list of elements with even index 
        for j in range(len(num_to_remove)):        
                text[i].remove(num_to_remove[j]) 

    if (isinstance(text[i],dict)):   #dictionary edit     
        text[i] = {k.upper(): text[i][k] for k in text[i].keys()}   

    if (isinstance(text[i],str)):  #string edit  
         text[i] = text[i][: len(text[i])//2]    

    i += 1      

pprint(text)            

           