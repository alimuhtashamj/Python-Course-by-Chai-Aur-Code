users = [
    {"name": "Ali", "age": 22, "degree": True},
    {"name": "Sara", "age": 19, "degree": True},
    {"name": "John", "age": 25, "degree": False},
    {"name": "Ayesha", "age": 28, "degree": True}
]

def extract_name(name,age,degree):
    extracted_names = []
    for i in users:
        if age >= 21 and degree:
          extracted_names += i
    return extracted_names