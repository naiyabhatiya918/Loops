#what is function?
#a function is a block of code that runs only when it is called.

#why use function?
#1. avoid code repetition
#2. makes program clean and organized
#3. easy to debug and reuse


#syntax of function:
# def function_name():
#     code


#example:

# def greet():
#     print("hello, students")
# greet()    #function call


#----------------------------------------------------------------------------------------

#function with parameters:
#used to pass values

# def greet(name):    #def greet(name="student") default parameter
#     print(f"hello, {name}!")
# greet("Naiya")    #function call with argument
# greet()    #function call without argument, will use default parameter value



#----------------------------------------------------------------------------------------


#function with return value:
#used when we want to send result back.

# def add(a, b):
#     return a + b

# result = add(2, 3)    #function call with arguments
# print(result)    



#--------------------------------------------------------------------------------



#task 1
#create a function to calculate and return result

num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
operator = input("choose operators(+,-,*,/)")
def cal(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
result = cal(num1,num2,operator)
print(f"result is {result}")
    
    





#task 2
#create a function to check if a number is even or odd with user input.

# num = int(input("enter a num:"))
# def even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# result = even_odd(num)
# print(result)



#task 3
#create a function to find the factorial of a number.

# num = int(input("enter a num:"))
# def fact(num):
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     return factorial 
# result = fact(num)
# print(result)


# num = int(input("enter a num:"))          #using recursion
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# result = fact(num)
# print(result)




#task 4
#craete a function to find maximum of three numbers.

# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# num3 = int(input("enter num3:"))

# def max(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:       
#         return num2
#     else:
#         return num3
# result = max(num1, num2, num3)
# print(f"maximum number is: {result}")



#task 5
#craete a function to check if a string is palindrome or not.
# strg = input("enter a string:")
# def palindrome(strg):
#     rev_strg = "".join(reversed(strg))
#     if strg == rev_strg:
#         return "palindrome"
#     else:
#         return "not palindrome"
# result = palindrome(strg)
# print(f"{strg} is {result}")

# strg = input("enter a string:")
# def palindrome(strg):
#     rev_strg = strg[::-1]
#     if strg == rev_strg:
#         return "palindrome"
#     else:
#         return "not palindrome"
# result = palindrome(strg)
# print(f"{strg} is {result}")




#task 6
# create a fumction to calculate the area of a circle. 

# radius = float(input("enter radius of circle:"))
# def area_radius(radius):
#     area = 3.14 * radius * radius
#     return area
# result = area_radius(radius)
# print(f"area of circle with radius {radius} is: {result}")



