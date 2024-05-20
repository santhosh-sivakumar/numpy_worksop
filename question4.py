#write a program to find the sum of digits of a given number'

def sod( n ):
  sum = 0
  while( n > 0 ):
    sum += ( n % 10 )
    n = ( n // 10 )
  return sum

a = int( input("Enter a Number: "))
print("The sum of the digits: ", sod(a))
