# This code demonstrates various basic operations you can do with Python lists.

# Create an empty list using a generic notation (note: the standard way is just list() or [])
empty_list = list[any]()
print(empty_list)  # Prints: []


# Create a list of fruits
fruits = ["apple", "banana", "cherry", "watermelon", "lemon"]

# Print the list and its length
print("fruits: ", fruits)                         # Show all items in the list
print("length of fruits: ", len(fruits))          # Show total number of items

# Accessing items in a list by index
print("first item of fruits: ", fruits[0])        # Show the first item (index 0)
print("last item of fruits: ", fruits[-1])        # Show the last item (negative index counts from end)

# Print a reversed version of the list (does not change original)
print("reverse fruits: ", fruits[::-1])           # Slice notation with a step of -1


# Modifying items in a list
print("before modifying: ", fruits)
fruits[0] = "pineapple"                           # Change the first item
print("after modifying: ", fruits)


# Accessing items specifically
print("accessing items: ", fruits[0])             # Access first item
print("accessing items: ", fruits[1])             # Access second item
print("last item: ", fruits[-1])                  # Access last item


# Slicing lists to select sublists
print("slicing items first 3: ", fruits[0:3])     # First three items (0,1,2)
print("slicing items from 1 to end: ", fruits[1:])# From second item to the end
print("slicing items first 3: ", fruits[:3])      # Alternate way to get first 3
print("slicing items last 3: ", fruits[-3:])      # Last three items
print("slicing items step 2: ", fruits[::2])      # Every other item
print("slicing items reverse: ", fruits[::-1])    # List reversed (as above)
print("reverse method: ", fruits.reverse())       # Actually reverses the list in place; returns None


# Check for the existence of an item
does_exist = "pineapple" in fruits                # Checks if "pineapple" is in the list
print("does exist: ", does_exist)


# Adding to a list
print("before append: ", fruits)
fruits.append("mango")                            # Add "mango" to end
print("after append: ", fruits)


# Inserting at a specific index
print("before insert: ", fruits)
fruits.insert(0, "mango")                         # Insert "mango" as the first element
print("after insert: ", fruits)


# Removing by index
del fruits[0]                                     # Delete first element
print("after remove: ", fruits)


# Removing last item (and returning it)
print("before pop: ", fruits)
fruits.pop()                                      # Remove last element
print("after pop: ", fruits)


# Clearing all items from a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()                                    # Remove all items
print(fruits)                                     # Prints: []

# Sorting a list
print("before sort: ", fruits)
fruits.sort()                                     # Sorts items alphabetically (list is empty here)
print("after sort: ", fruits)


# Reversing a list
print("before reverse: ", fruits)
fruits.reverse()                                  # Reverses the items in place
print("after reverse: ", fruits)

# Concatenating lists (joining lists)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers     # Combine the lists
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables               # Join two lists
print(fruits_and_vegetables)


# Joining lists with extend (adds all elements from another list)
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6, 7]
num1.extend(num2)                                 # Adds items from num2 to num1
print("after extend: ", num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
print("join negative and positive numbers: ", negative_numbers + positive_numbers)


# Counting occurrences
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))                     # How many times 'orange' occurs
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))                             # How many times 24 appears


# Finding the index of an item
print("index of orange: ", fruits.index("orange"))


# Reversing and checking value returned by reverse() (it returns None)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()                                 # Reverses in place
print("reverse fruits: ", fruits.reverse())      # Already reversed, but print returns None


# Sorting in-place ascending and descending
fruits.sort()                                    # Sort alphabetically
print("sort: ", fruits)

fruits.sort(reverse=True)                        # Sort in reverse alphabetical order
print("sort reverse: ", fruits)