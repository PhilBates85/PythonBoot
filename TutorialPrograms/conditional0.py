age = int(input("How old are you: "))
minimum = 17
if age > minimum:
    print('You are old enough to drive')
else:
    print('Keep waiting Jr.')
# first problem I had was not defining the input as an integer so
# when the program asked to compare it caused an error bc
# two strings cant be compared with =,<,>
#adding int to the beginning resolved this
# second problem was the return statements Print vs print are case sensative
