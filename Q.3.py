# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.
pw=input("Enter the password: ")
pw1=input("Enter the password again: ")
if (len(pw)>=8 and len(pw)<=12):
    if pw==pw1:
        print("Password set")
    else:
        print("Password does not match")
else:
    print("Not enough character")