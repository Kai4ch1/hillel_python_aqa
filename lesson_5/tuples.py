#Для зберігання тестових даних, займають меньше місця
my_tuple = (1, 2)


tuple_of_names = ('Igor', 'Vitia')
tuple_of_tuples =((1, 2), ("2", "-1"))

mixed_tuple = (1, "b", False, True, tuple_of_names)

#nuances

names = ("1") # That will be a string
nums = 33, 5 # also tuple
names_1 = "qwe", "qwe" # also tuple

print(type(names))

#modify var to tuple

my_name = 'Aoi'

my_name_tuple = tuple(my_name)
print(my_name_tuple)

#tuple by index
print(my_name_tuple[-1])
print(my_name_tuple[1:])

t2tuple = (1, 2, 3, 2, 2, "qwe") #works with mixed tuple
print(t2tuple[-1])
print(t2tuple[-1][-1]) #parse the tuple, then parse the element

#count

print(t2tuple.count(2))

#Index

print(t2tuple.index("qwe"))

