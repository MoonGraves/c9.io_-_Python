import re
def valid_user_name(s):

        return re.fullmatch(r"[a-z\d][3,10]", s)
        
user_name = input("User name??")

#User regual expression to test that user_name is
#3 to 10 characters in length
#oly contains characters a-z , 0-9

if valid_user_name(user_name):
    print("user name ok")
    
else:
    print("Invalid user name")
    
