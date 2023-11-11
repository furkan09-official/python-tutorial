# dictionary methods
dict = {1:'Python' , 2:'Java' , 3:'C' , 10:'Rust'}

dict1 = dict.copy()
print(dict1)

dict.clear()
print(dict)

print(dict1.get(10))

print(dict1.items())

print(dict1.keys())

print(dict1.values())

dict1.update({3:'java script'})
print(dict1)

dict1.pop(1)
print(dict1)

