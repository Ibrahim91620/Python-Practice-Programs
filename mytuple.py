# tup: similar to list. tuples are unchangeable meaning 
# we can not alter them after creation
# tupples are immutable
tup=(1,2,3,4,5,"green",True)

print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])

if "sd" in tup:
    print("yes it is present")
else:
    print("Not present")
tup2=tup[1:]
print(tup2);