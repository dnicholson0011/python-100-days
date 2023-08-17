# List Methods:

# append(item): Adds an item to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print("#1 append: " + str(my_list))  # Output: [1, 2, 3, 4]

# extend(iterable): Adds all the elements of an iterable (like a list or a tuple) to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print("#2 extend: " + str(my_list))  # Output: [1, 2, 3, 4, 5, 6]

# insert(index, item): Inserts an item at a specific position in the list.
my_list = [1, 2, 4]
my_list.insert(2, 3)  # Insert the number 3 at index 2
print("#3 insert: " + str(my_list))  # Output: [1, 2, 3, 4]

# remove(item): Removes the first occurrence of an item from the list.
my_list = [1, 2, 3, 2]
my_list.remove(2)  # Remove the first occurrence of 2
print("#4 remove: " + str(my_list))  # Output: [1, 3, 2]

# pop(index): Removes and returns the item at a specific position in the list. If no index is specified, it removes and returns the last item in the list.
my_list = [1, 2, 3]
item = my_list.pop(1)  # Remove and return the item at index 1
print("#5 pop: " + str(item))  # Output: 2
print("#5 my_list: " + str(my_list))  # Output: [1, 3]

# index(item): Returns the index of the first occurrence of an item in the list.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print("#6 index: " + str(index))  # Output: 1

# count(item): Returns the number of times an item appears in the list.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print("#7 count: " + str(count))  # Output: 2

# sort(): Sorts the items in the list in ascending order.
my_list = [2, 1, 3, 2]
my_list.sort()
print("#8 sort: " + str(my_list))  # Output: [1, 2, 2, 3]

# sort(): Sorts the items in the list in descending order.
my_list = [2, 1, 3, 2]
my_list.sort(reverse=True)
print("#9 sort: " + str(my_list))  # Output: [3, 2, 2, 1]

# reverse(): Reverses the order of the items in the list.
my_list = [1, 2, 3]
my_list.reverse()
print("#10 reverse: " + str(my_list))  # Output: [3, 2, 1]

# clear(): Removes all items from the list.
my_list = [1, 2, 3]
my_list.clear()
print("#11 clear: " + str(my_list))  # Output: []
