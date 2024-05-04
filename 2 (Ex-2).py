# Exercise 2
my_lst = [5, 1, 8, 3, 2]
if len(my_lst) < 2:
    print("The list must contain at least 2 elements!")
else:
    my_lst.sort()
    new_lst = my_lst[1:-1]
    print("The new list is:", new_lst)

my_lst2 = [3, 7, 2, 9, 4, 6]
if len(my_lst2) < 2:
    print("The list must contain at least 2 elements!")
else:
    my_lst2.sort()
    new_lst = my_lst2[1:-1]
    print("The new list is:", new_lst)
