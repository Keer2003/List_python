def encypt_func(words , s):  
    result = ""  
  

    for i in range(len(words)):  
        char = words[i]  
       

    if (char.isupper()):  
           result += chr((ord(char) + s - 64) % 26 + 65)  


    else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  

words = input("Element it service") 
s = 1 
  
print("Plain txt : "+words ) 
print("Shift pattern : "+s ) 
print("Cipher: " encrypt_func+words,s )
