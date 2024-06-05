import time

hour=time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
# greet=time.strftime('%H,%M,%S')
# hour=int(input("Enter hour: "))

# print(hour)

if(hour>=0 and hour<12):
    print("Good morning sir!")

elif(hour>=12 and hour<15):
    print("Good Afternoon")
elif(hour>=15 and hour<18):
    print("Good evening!!")
elif(hour>=18 and hour<0):
    print("Good Night!!")

