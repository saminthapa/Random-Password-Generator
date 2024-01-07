import random
charaters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
pass_length = int(input("Enter the length of your password:- "))
pass_count = int(input("Enter the number of password you want:- "))
for i in range (0, pass_count):
    password = ""
    for j in range(0, pass_length):
        pass_char = random.choice(charaters)
        password = password+pass_char
    print("Your password in ready:-",password)       
