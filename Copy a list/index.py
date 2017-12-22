# The following merely makes y an alias for the object identified as x
print('Alias')
print('before...')
x = [('a', 1), 2, 3]
y = x
print(f'x -> {x}') # [1, 2, 3]
print(f'y -> {y}') # [1, 2, 3]

# Adding an element to y adds the element to x too
y.append(4)
print('after...')
print(f'x -> {x}') # [1, 2, 3, 4]
print(f'y -> {y}') # [1, 2, 3, 4]

# The following makes a shallow copy of x and assigns the new list instance to y
print("\nShallow copy")
print('before...')
x = [['a', 1], 2, 3]
y = list(x)
print(f'x -> {x}') # x -> [['a', 1], 2, 3]
print(f'y -> {y}') # y -> [['a', 1], 2, 3]

# Adding an element to y does NOT add the element to x
y.append(4)
print('adding an element to y does NOT add the element to x...')
print(f'x -> {x}') # x -> [['a', 1], 2, 3]
print(f'y -> {y}') # y -> [['a', 1], 2, 3, 4]

# However, mutating an object in y DOES mutate the same object in x
y[0][0] = 'b'
print('However, mutating an object in y DOES mutate the same object in x...')
print(f'x -> {x}') # x -> [['b', 1], 2, 3]
print(f'y -> {y}') # y -> [['b', 1], 2, 3, 4]

# The following makes a deep copy of x and assigns the new list instance to y
import copy

print("\nDeep copy")
print('before...')
x = [['a', 1], 2, 3]
y = copy.deepcopy(x)
print(f'x -> {x}') # x -> [['a', 1], 2, 3]
print(f'y -> {y}') # y -> [['a', 1], 2, 3]

# Adding an element to y does NOT add the element to x
y.append(4)
print('adding an element to y does NOT add the element to x...')
print(f'x -> {x}') # x -> [['a', 1], 2, 3]
print(f'y -> {y}') # y -> [['a', 1], 2, 3, 4]

# Mutating an object in y does NOT mutate the same object in x
y[0][0] = 'b'
print('Mutating an object in y does NOT mutate the same object in x...')
print(f'x -> {x}') # x -> [['a', 1], 2, 3]
print(f'y -> {y}') # y -> [['b', 1], 2, 3, 4]
