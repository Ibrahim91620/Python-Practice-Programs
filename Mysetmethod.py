# set method

s1={"class","ibrahim"}
s2={"ibrahim","washim","shams"}
# print(s1.union(s2))

# s1.update(s2)

# print(s1,s2)

# s1.intersection_update(s2)

# print(s1)


print(s1.symmetric_difference(s2))
# symmetric_difference means that union minus intersection 


# difference --A-B sets
s1.discard("ibrahi")
print(s1)

item=s1.pop()
print(item)

del s1 
# it delete the whole set

print(s1)












