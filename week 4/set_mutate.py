# mutable, items can be added or removed, but not modified
set = {1, "23", 4.5687}

set.add("wow") # works

print(set)

set[2] = 90 # will cause error

print(set)