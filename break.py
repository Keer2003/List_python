try:
    var=1
    while var<6:
        print(var)
        if var==3:
            break
        var+=1
except Exception as e:
    print(e)
