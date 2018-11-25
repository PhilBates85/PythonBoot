x = 0
while x < 3:
    print("Smaller")
    x = x + 1

print("Password Checker Program")

correct_password = "python123"
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter Again: ")

print("Logged in")
