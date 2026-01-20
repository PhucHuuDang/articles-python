print("Hello, World!")

# variables
name = "Harry"
age = 24

height = 1.75

is_student = True

print(name, age)

numbers = [1,2,3,4,5]

names = ["harry", "john"]

mixed = [1, "harry", 3.12, True]



print("getting the second name: ", names[1])

numbers.append(6) # append 6 to the end of the list

numbers.insert(1, 10) # insert 10 at index 1

print("numbers after append and insert: ", numbers)
numbers.remove(6) # remove 6 from the list
numbers.pop() # remove the last element from the list
numbers.pop(1) # remove at index

print("count : ", numbers.count(10))



for name in names:
  print(name)


for i, name in enumerate(names):
  print(f"index: {i}, name: {name}")


# Array objects

users = [
  {
    "id": 1, "name": "harry", "age": 24
  },
  {
    "id": 2, "name": "john", "age": 25
  },
  {
    "id": 3, "name": "jane", "age": 26
  }
]

print("users: ", users[0]['name'])

for user in users:
  print(user['name'])

for user in users:
  print(f"id: {user['id']}, name: {user['name']}, age: {user['age']}")

for user in users:
  print(f"id: {user['id']}, name: {user['name']}, age: {user['age']}")



user = {
  "id": 1, "name": "harry", "age": 24
}

user['age'] = "Harry Dang"


print("user: ", user)

del user['age']

print("after deleting age: ", user)

user.update({"name": "John Doe"})

print("get name", user.get("name"))

print(user.setdefault("email", "harry@gmail.com"))

print("updated user: ", user)
print("keys: ", user.keys())


# browse objects 

for key in user:
  print("key: ", user[key])

for key, value in user.items():
  print("key: ", key, "value: ", value)


posts = [
  {
    "id": 1, "title": "python", "tags": ["programming", "python"]
  },
  {
    "id": 2, "title": "javascript", "tags": ["programming", "javascript"]
  },
  {
    "id": 3, "title": "java", "tags": ["programming", "java"]
  },
  {
    "id": 4, "title": "c#", "tags": ["programming", "c#"]
  },
  {
    "id": 5, "title": "c++", "tags": ["programming", "c++"]
  }
]



for post in posts:
  print("post: ", post['title'])




