import re
 
 
def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list
 
# Driver code
 
 
list = ['4geeks', '3for', '4geeks']
print(remove(list))
