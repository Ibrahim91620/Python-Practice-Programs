def func1():

 try:
   
    l=[1,2,3,4,5]

    i=int(input("Enter the index of array:"))

    print(l[i])
    return 1
 except:
    print("Some error occurred")
    
    return 0
 finally:
    print("I am finally and it always executed")
# if you want to close the connection of database,file system
# then you have to write the code inside the finally
x=func1()
print(x)