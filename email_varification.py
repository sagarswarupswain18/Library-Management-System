dmain='.com'
def email_varification(email):
    if email[0].isalpha()==True and email.islower()==True and email.count('@')==1 and email.count(' ')==0 and email[-4:]==dmain and len(email)>7:
        return 1
    else:
        return 0
