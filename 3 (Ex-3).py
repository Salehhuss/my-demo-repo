# Exercise 3
my_lst = input("Enter a list of 5 characters: ")
if len(my_lst) != 5:
    print("This list doesn’t have the right size")
else:
    lst = list(my_lst)
    string = lst[0] + lst[1] + lst[2] + lst[3] + lst[4]
    print("The string is:", string)


