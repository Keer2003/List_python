try:
    cnt=0
    var="elegent software traning"
    while cnt<len(var):
        if var[cnt]=='e' or var[cnt]=='s':
            cnt +=1
            continue
        print("count letter:",var[cnt])
        cnt+=1
except Exception as e:
    print(e)
