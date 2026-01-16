# You have a list of user dictionaries, each with "name" and "score".

# Write a function passing_users(users) that returns a list of names whose score is ≥ 50.

# Use a lambda function and list comprehension for filtering.

users = [
    {"name": "Alice", "score": 45},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 60}
]

def passing_users(users):
     check = lambda users : users['score'] >= 50
     return [user['name'] for user in users if check(user)]
result = passing_users(users)
print(result)
    