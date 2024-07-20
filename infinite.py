try:
    age=28
    while age>19:
        print("Infinite loop")
except Exception as e:
    print(e)
        
try:
    cnt=0
    var="elegent software traning"
    while cnt<len(var):
        if var[int]=='e' or var[cnt]=='s':
            cnt +=1
            continue
        print("count letter:",var[cnt])
        cnt+=1
except Exception as e:
    print(e)

