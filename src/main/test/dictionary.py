# Dictionary Methods:

# get(key, default): Returns the value for a key if it exists in the dictionary. If not, it returns the default value.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("#1 get: " + str(my_dict.get('b', 'default')))  # Output: 2
print("#1 get: " + str(my_dict.get('d', 'default')))  # Output: default

# keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("#2 keys: " + str(list(my_dict.keys())))  # Output: ['a', 'b', 'c']

# values(): Returns a view object that displays a list of all the values in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("#3 values: " + str(list(my_dict.values())))  # Output: [1, 2, 3]

# items(): Returns a view object that displays a list of the dictionary's key-value tuple pairs.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("#4 items: " + str(list(my_dict.items())))  # Output: [('a', 1), ('b', 2), ('c', 3)]

# update(other): Updates the dictionary with the key-value pairs from other, overwriting existing keys.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'b': 20, 'd': 4})
print("#5 update: " + str(my_dict))  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# pop(key): Removes and returns the value for a key from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print("#6 pop: " + str(value))  # Output: 2
print("#6 my_dict: " + str(my_dict))  # Output: {'a': 1, 'c': 3}

# popitem(): Removes and returns a (key, value) pair from the dictionary. Pairs are returned in LIFO (Last In, First Out) order.
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print("#7 popitem: " + str(item))  # Output: ('c', 3)
print("#7 my_dict: " + str(my_dict))  # Output: {'a': 1, 'b': 2}

# setdefault(key, default): Returns the value of a key if it exists in the dictionary. If not, inserts the key with a default value and returns the default value.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('d', 4)
print("#8 setdefault: " + str(value))  # Output: 4
print("#8 my_dict: " + str(my_dict))  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# clear(): Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print("#9 clear: " + str(my_dict))  # Output: {}
