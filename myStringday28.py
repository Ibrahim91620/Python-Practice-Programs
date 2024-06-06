# String formatting in python


country="India"
name="ibrahim"

letter="hey my name is {} and i am from {}"
print(letter)

print(letter.format(name,country))

print(f"hey my name is {name} and i am from {country}")


txt="the price of apple {price:.2f} rupees`"
print(txt.format(price=50.4543)) 
# it is done through format method

price=122.343
txt=f"the price of apple is: {price:.2f}"
print(txt)

# if we want to print {} in python

print(f"hello my name is  {{name}} and i am from {{countrty}}")