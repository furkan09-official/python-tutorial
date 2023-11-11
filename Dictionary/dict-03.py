# Accessing the elements from the dictionary

dict = {1:'Indian' ,2:'motor' ,3:'training' , 4:'school' , 'sanchalak':'sandeep shrivstava'}
print(dict[1])
print(dict[4])
print(dict['sanchalak'])

# using the get() method  this method accept the key as an argument and return the value

dict  = {1:'the ' , 2:'vikings' , 3:'vellhalla' , 'season':2}
print(dict[3])
print(dict.get(2))

# Accessing the element of an nested dictionary
dict = {1:{'a':'romi' , 'b':'baba farid','c':{'A':'kabir'}}}
print(dict[1]['b'])
print(dict[1]['c']['A'])