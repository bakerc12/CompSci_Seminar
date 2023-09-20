#Differences between lists and arrays:
# the differences between lists and arrays include that lists contain elements of different data types while arrays contain elements of the same data types.
# Another difference that I found is that lists cannot do arithmetic equations while arrays can.
#list = [13,"thirteen", 0.13]
#this list printed a string, integer, and a float.
#lists can contain integers, strings, floats, bools, and true at the same time.
#to create an empty list you would create a variable and then make it equal to square brackets with nothing in them
lst = []
print (lst, "this is an empty list")
#this is an empty list
# to add an element to a list, you would a do lst.append and then in () after append, you put what ever element you want to add to the end of the list
lst.append("test")
print(lst, "this list has an element added to the end")
#this adds "test" to the end of the empty list
#All elements in lists are ordered by numbers starting at 0. this means that if I have a list of numbers [1,2,3,4,5] the number 1 is equal to the 0th element in the index.
#to access a specific element from the list index you would use:
lst_2 = [1,2,3,4,5]
print ("(",lst_2[0],")","By using [0] in the () is specifies which element to print, in this case, the number 1 corresponds to the 0th term in the list ")
#how to print all of the items in a list using a for loop.
lst_3 = [1,2,3,4,5,6]
for i in range(0,6):
    print (lst_3[i])
# this prints the list in different rows
#to find the length of a list you would use the term "len" in your code
lst_4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#then make a variable called "list length" and make it equal to "len(lst_4)" (or whatever the list is called in your code)
list_length = len(lst_4)
#then you would print the variable
print("your list length is", list_length)
#this gives you the length of the list
#to find the sum of all of the numbers in a list using a for loop, you first have to make a variable to hold the sum of the numbers
sum_of_lst_4 = 0
#then you have to create the for loop with the name of the list being used so that the program can determine what to find the sum of.\
#use the plus sign to show that you just want to add all of the numbers together
for num in lst_4:
    sum_of_lst_4 += num
#then you have to print the sum
print("The sum of the numbers is", sum_of_lst_4)
#what is a nested for loop
#a nested for loop is just another loop inside of the for loop. This can be achieved by using square brackets within sscquare brackets to make a two dimentional loop
#nested for loops can be used for puzzles/board games. With puzzles and games, the nested for loop can be used to check for correct moves or to decide who wins
