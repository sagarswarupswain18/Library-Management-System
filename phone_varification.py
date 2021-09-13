def phone_varification(phone):
    t=0
    while(phone!=0):
        t+=1
        phone=phone//10
    if t==10:
        return 1
    else:
        return 0