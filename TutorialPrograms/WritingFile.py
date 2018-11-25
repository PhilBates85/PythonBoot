 myfile = open("employee.txt", "w")
 myfile.write("Phil")
 myfile.close()

 myfile = open("employee.txt", "w")
 myfile.write("Phil\nMike\nBob\nNiko")
 myfile.close()

myfile = open("employees2.txt", "a")
myfile.write("\nJack")
myfile.close()
