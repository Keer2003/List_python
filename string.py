try:
    tempstr="Wecome 2 Python World 123!"
    numcnt,ucnt,scnt=0,0,0
    for echar in tempstr:
        print(echar)
        if echar.isdigit():
            numcnt+=1
        elif echar.isspace():
            scnt+=1
            
            
