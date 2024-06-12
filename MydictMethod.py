dict={
    
    "name": "ibrahim",
    "roll" : "mmca003hy",
    "course" :"mca"

}
print(dict)
# The update() method updates the value of the key provided to it if the item already 
# exists in the dictionary, else it creates a new key-value pair.
dict.update({'name':'faizi'})
dict.update({'roll':"23"})
print(dict)

# There are a few methods that 
# we can use to remove items from dictionary.
dict.clear()
print(dict)

# The pop() method removes 
# the key-value pair whose key 
# is passed as a parameter.

dict.pop('course')
print(dict)



