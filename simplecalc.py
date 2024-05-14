def add(x,y):
 return x+y
def subtract(x,y):
 return x-y
def multiply(x,y):
 return x*y
def divide(x,y):
 return x/y
print("Apply the operation to calculate the numbers. ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter the choice to calculate numbers: "))
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if choice == 1:
  print(num1 ,"+", num2 ,"=",add(num1,num2))
elif choice == 2:
  print(num1 ,"-", num2 ,"=",subtract(num1,num2))
elif choice == 3:
  print(num1 ,"*", num2 ,"=",multiply(num1,num2))
elif choice == 4:
  print(num1 ,"*", num2 ,"=",divide(num1,num2))
else:
  print("This is a invalid input")

