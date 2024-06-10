def factorial(n):
    fact=1
    
    for i in range(1,n+1,1):
     fact=fact*i

    print(fact)

    
factorial(5)
# recursion
def factorial(n):
   if(n==0 or n==1):
      return 1

   else:
      return n*factorial(n-1)

print(factorial(3))  
print(factorial(5))  
print(factorial(6))  
print(factorial(0))  


# fibonnaci series

def fibonnaci(n):
   if(n==0):
      
    return 0
   else:
      return fibonnaci(n-1)+fibonnaci(n-2);

print(fibonnaci(5))
