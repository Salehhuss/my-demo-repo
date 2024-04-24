# Exercise 6
string = input("Enter a string (maximum size of 5): ")
length = len(string)

if length == 1:
    print(string * 6)
elif length == 2:
    print(string[1] + string[0])
elif length == 3:
    print(string[2] + string[:2])
elif length == 4:
    print(string[::-1])
elif length == 5:
    print(string[0] + "t" + string[1] + "t" + string[2] + "t" + string[3] + "t" + string[4])
