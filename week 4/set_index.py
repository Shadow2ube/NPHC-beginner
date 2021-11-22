# items cannot be accessed with []
set = {1, "23", 4.5687}

print(set[0]) # will cause error

# but this will not

a, b, c = set

print(a)
print(b)
print(c)
