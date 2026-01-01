# a function that greets a user even if no name is provided
def greet(name):
    return 'Hey ' + name + '!'
g = greet('Ali')
print(g)

def greet( name = 'User'):
    return 'Hey ' + name + '!'
g = greet()
print(g)