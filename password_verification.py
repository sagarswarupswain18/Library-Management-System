def password_verification(pas):
    #pas = input('enter password')
    l = u = s = n = 0
    spl = ['!','@','#','%','$','&']
        
    if ((len(pas)>=6)and(len(pas)<=12)):
        for val in pas:
            if ord(val) in range(65,91):
                l+=1
                continue
            if ord(val) in range(97,122):
                u+=1
                continue
            if val in spl:
                s+=1
                continue
            if int(val) in range(9):
                n+=1
                continue
        if l>0 and u>0 and s>0 and n>0:
            return 1
        else:
            return 0
    return 0
