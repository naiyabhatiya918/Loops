# #date: 18-03-2026
# #what is a loop?
# #a loop is used to repeat a block of code until a certain condition is met.
# #types of loops in python
# #1. for loop
# #used when e know how many times we want to repeat a block of code

# #syntax of for loop
# # for variable in sequence:
# #     code

# #range() function is commonaly used to generate a sequence of numbers.
# #range comes with three parameters:
# #1.start (inclusive)
# #2.stop (exclusive)
# #3.step (optional, default is 1)

# #range(start, stop, step)

# #example:
# for i in range(1, 5):
#     print(i)

# #key points:
# #1. range(start, stop) generates numbers
# #2. loop runs fixed num of times.


# #-------------------------------------------------------------------------------------



# #2. while loop
# #used when we repeat until a condition becomes false.

# #syntax of while loop
# # while condition:
# #     code

# #example:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# #o/p: 1 2 3 4 5

# #key points:

# #loop control statements:

# #1. break: 
# # stops the loop immediately

# #example:
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# #o/p: 1 2


# #2. continue:
# #skips the current iteration 

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# #o/p: 1 2 4 5


# #3. pass:   
# #does nothing(placeholder)

# for i in range(5):
#     pass




#task 1
#print numbers from 1 to 10 using for loop
# for i in range(1,11):
#     print(i, end=" ")




#task 2
# print even numbers from 1 to 20 using for loop
# for i in range(1,21):     # way 1
#     if i % 2 == 0:
#         print(i, end=" ")

# for i in range(2, 21, 2):       # way 2
#     print(i, end=" ")




#task 3
# print odd numbers from 1 to 15 using for loop
# for i in range(1,16):  # way 1
#     if i % 2 != 0:
#         print(i, end=" ")

# for i in range(1, 16, 2):    # way 2
#     print(i, end=" ")


# for i in range(21,1,-2):    #decending order in odd num
#    print(i, end=" ")


#task 4
# print each character of a string.

# txt = "python"
# for char in txt:
#     print(char)


#task 5
# print all items in the list

# data = ["data", "science", "AI"]
# for items in data:
#     print(items)


#task 6
#find the sum of numbers from 1 to 10.

# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)


#task 7
# print multiplication table of 5.  (f means formatted strings
# allow embedding expressions inside string literals.)

# for i in range(1,11):      #num declare kari ne 5 ni jagya pr lakhi sakay chhe
#     print(f"5 x {i} = {5*i}")


#task 8
#count how many vowels are in a string.

# txt = "hello world"
# vowel_count = 0
# for char in txt:
#     if char in 'aeiouAEIOU':
#         vowel_count += 1
# print(f"number of vowels: {vowel_count}")


#task 9
#print numbers in reverse order from 10 to 1.

# for i in range(10, 1, -1):
#     print(i, end=' ')


#task 10
# print square of numbers from 1 to 5.
for i in range(1, 6):
    print(f" sqare of {i} is {i**2}")