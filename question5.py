#write a program to find if the given number is prime no or not

def prime(n):
    for i in range( 2, n//2 + 1 ):
        if ( n % i == 0):
            return False
    return True

a = int( input("Enter a Number: "))
if( prime(a) ):
    print("Number is Prime")
else:
    print("Number is not Prime")
