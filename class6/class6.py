# Lists, tuples and dictionaries can be converted to set
# Split it and sort it alphabetically

set1 = set([1, 3, 2, 4])
print(set1)

set2 = set(range(10))
print(set2)

set1.update({0, 10, 20})
print(set1)
print(len(set1))

print(set1.discard(1))  # It does not return nothing
print(set1.remove(20))  # It does not return nothing
print(set1)

print(2 in set1)  # Corroborate if the number is inside the set
set1.clear()
print(set1)  # Clears the set, remove the data

set1.update({1, 2, 3, 4, 5, 6})
set1.pop()
print(set1) # Pop does not delete the last index due the set is not sorted



