username= "admin"
password = "password123"

user = input("What is your username?")
userpass = input("What is your password?")
if user == username and userpass == password: 
    print("access granted")
else: 
    print("Error Access Denied")
