# Tuple Methods:

# Tuples in Python are similar to lists, but they are immutable,
# meaning that once they are created, they cannot be modified.
# Because of this, tuples do not have methods like append(), extend(), insert(), remove(), pop(), sort(), reverse(), and clear()

# count(item): Returns the number of times an item appears in the tuple.
my_tuple = (1, 2, 3, 2)
count = my_tuple.count(2)
print("#1 count: " + str(count))  # Output: 2

# index(item): Returns the index of the first occurrence of an item in the tuple.
my_tuple = (1, 2, 3, 2)
index = my_tuple.index(2)
print("#2 index: " + str(index))  # Output: 1
