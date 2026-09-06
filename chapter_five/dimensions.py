#when defining a tuple,the collection numbers is enclosed in parenthese () instead of square brackets [].
dimensions = (200,500)
print(dimensions[0])
print(dimensions[1])

#Tuples are immutable,so attempt to assign a new value to an element raise a TypeError
dimensions = (200,50)
dimensions[0] = 250


#You can iterate over tuples using the same for-loop syntax as lists
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)


#you can't assign to individual tuple items,but you can reassign the variable to a new tuple.
dimensions = (200,500)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

#4-13.Buffet:A bufft-style restaurant offers only five basic foods.Think of five simple foods,and store them in a tuple.
menu = ('Egg','Bacon','Sandwich','Italian noodles','French fries')
#Use a for loop to print each food the restaurant offers.
for item in menu:
    print(item)
#Try to modify one of the items,and make sure that Python reject the change
#menu[0] = "Hamburger"

menu = ('Hamburger','Fried shrimp','Sandwich','Italian noodles','French fries')