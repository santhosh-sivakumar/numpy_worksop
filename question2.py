# find if the given number is a palindrome or not?

a = input("Enter a Number: ")

if( a == a[::-1] ):
  print("Given Input is Palindrome")
else:
  print("Given Input is Not a Palindrome")
