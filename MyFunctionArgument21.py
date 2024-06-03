# def subtract(a,b):
#     if(a>b):
#         print(a-b)
#     else:
#         print(b-a)

# a=8
# b=10
# subtract(a,b)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        # return sum/len(numbers) //wps lekr chle jao uss value ko
    
c=average(1,2,3,4,5)
print(c)
