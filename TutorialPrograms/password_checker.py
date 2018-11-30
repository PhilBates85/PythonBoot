x = 0
while x < 3:
    print("Smaller")
    x = x + 1

print("Password Checker Program")

correct_password = "python123"
name = input("Enter your first name: ")
lastName = input("Enter your last name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter Again: ")

message = "Hello %s %s, you are now Logged in" %(name, lastName)
print(message)
