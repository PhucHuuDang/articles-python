# single

letter = "p"

print(letter)

print(len(letter))

first_name = "Harry"
last_name = "Dang"

first_name.removeprefix("H")
print(first_name)


print(first_name[-1])

last_index = len(first_name) -1 
print(first_name[last_index])


# slicing

language = 'python'

print("slicing: ", language[0:3])
print("slicing: ", language[1:])
print("slicing: ", language[:3])
print("last 3 characters: ", language[-3:])

print('Day 1\t3\t5')
print("step: ", language[::2])
print("step: ", language[::-1])

print("reverse: ", language[::-1])
print("reverse: ", language[::-2])
print("reverse: ", language[::-3])
print("reverse: ", language[::-4])
print("reverse: ", language[::-5])
print("reverse: ", language[::-6])
print("reverse: ", language[::-7])


# utility methods

hey = "hey"

print("capitalize: ", hey.capitalize())
print("upper: ", hey.upper())
print("lower: ", hey.lower())
print("title: ", hey.title())
print("swapcase: ", hey.swapcase())
print("casefold: ", hey.casefold())
print("center: ", hey.center(10))
print("ljust: ", hey.ljust(10))
print("rjust: ", hey.rjust(2))
print("strip: ", hey.strip())
print("lstrip: ", hey.lstrip())
print("rstrip: ", hey.rstrip())
print("replace: ", hey.replace("h", "j"))



# format methods

name = "Harry"
age = 24

print("name: {name}, age: {age}".format(name=name, age=age))
print("name: {0}, age: {1}".format(name, age))
print("name: {0}, age: {1}".format(age, name))
print("name: {1}, age: {0}".format(name, age))
print("name: {1}, age: {0}".format(age, name))
print("name: {1}, age: {0}".format(age, name))

print("start with: ", name.startswith("H"))
print("end with: ", name.endswith("y"))
print("index: ", name.index("a"))
print("rindex: ", name.rindex("a"))
print("find: ", name.find("a"))
print("rfind: ", name.rfind("a"))
print("count: ", name.count("a"))
print("replace: ", name.replace("a", "b"))
print("split: ", name.split("a"))
print("join: ", name.join("a"))
print("join: ", name.join("a"))


# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

print("expandtabs: ", name.expandtabs(10))


# find(): Returns the index of first occurrence of substring


print('name', name.find("a")) # the index of the first occurrence of 'a'


# isalnum(): Checks alphanumeric character

print("isalnum: ", name.isalnum())
print("isalpha: ", name.isalpha())
print("isdigit: ", name.isdigit())
print("isspace: ", name.isspace())
print("isupper: ", name.isupper())
print("islower: ", name.islower())
print("istitle: ", name.istitle())
print("isprintable: ", name.isprintable())
print("isidentifier: ", name.isidentifier())
print("isdecimal: ", name.isdecimal())
print("isnumeric: ", name.isnumeric())


# split

print("split: ", name.split())
print("split: ", name.split("a"))
print("split: ", name.split("a", 1))
print("split: ", name.split("a", 2))
print("split: ", name.split("a", 3))
print("split: ", name.split("a", 4))
print("split: ", name.split("a", 5))
print("split: ", name.split("a", 6))
print("split: ", name.split("a", 7))
print("split: ", name.split("a", 8))
print("split: ", name.split("a", 9))


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name | its will be false if it contains spaces or special characters and numbers at the beginning

print("isidentifier check: ", name.isidentifier())

# isupper(): returns if all characters are uppercase characters
print("isupper check: ", name.isupper())

# swapcase(): Checks if String Starts with the Specified String
print("swapcase check: ", name.swapcase())

# title(): Converts the first character of each word to uppercase
print("title check: ", name.title())

# capitalize(): Converts the first character of the string to uppercase
print("capitalize check: ", name.capitalize())

# casefold(): Converts the string to lowercase
print("casefold check: ", name.casefold())
