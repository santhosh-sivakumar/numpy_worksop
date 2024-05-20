#write a program to find the factorial of a nummber

def fact(n):
  if n == 1 or n == 0:
      return n
  else:
      return n * fact( n - 1 )

a = int( input("Enter a Number: "))
print("The Factorial: ", fact(a) )
