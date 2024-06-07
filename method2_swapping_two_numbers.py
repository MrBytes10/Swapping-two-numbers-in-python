# Now instead putting the numbers, we collect input from the user
num1=input("Enter num1 value:")
num2=input("Enter num2 value:")

print("value of num1 before swapping is:",num1) # comma is a concatenation operator
print("value of num2 before swapping is:",num2)

temp= num1 # temp means temporary value, which is 50 now
num1= num2 # num1 is 100 now
num2= temp # num2 is 50 now

print("\nvalue of num1 after swapping is:",num1) # comma is a concatenation operator
print("value of num2 after swapping is:",num2)