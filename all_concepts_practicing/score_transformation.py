# Problem:

# Input: List of users 

# Goal: Create a new list of dictionaries, where each user’s score is scaled to 0–1 (divide by 100)

# Output: List of dictionaries with name and normalized score

users = [
    {"name": "Alice", "score": 45},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 60}
]

def transform(data):
    transformation = lambda user: {'name': user['name'], 'score' :user['score'] / 100}
    return [transformation(user) for user in users]
print(transform(users))