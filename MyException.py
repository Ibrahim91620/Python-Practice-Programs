a=int(input("Enter a number for printing a table"))

try:
    for i in range(1,11):

     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
   print(e)

print("it show some errors")





