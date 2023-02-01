ages = [10, 15, 20]

# add a new element at the end of the list
ages.append(15)

# remove the first occurrence of an element
ages.remove(15)

# remove the last element and return it 
removed_element = ages.pop()
print(removed_element) # print 15

# remove the element by index
removed_element = ages.pop(0)
print(removed_element) # print 10

# return True if an element is in the list 
print(20 in ages) # print True
print(30 in ages) # print False

# insert element in specific index
ages.insert(0, 15)
print(15 in ages) # print True

# insert a list inside the list 
ages.append([40, 50])
print([40, 50] in ages) # print True

# extending a list 
ages.extend([40, 50])
print(ages) # print 15, 20, [40, 50], 40, 50

ages.remove([40, 50])

# list comprehension
even_ages = [number for number in ages if number % 2 == 0]
print(even_ages)

odd_ages = [age for age in ages if age not in even_ages]
print(odd_ages)

ages_in_the_next_year = [age + 1 for age in ages]
print(ages_in_the_next_year)

# remove all items from the list 
ages.clear()
print(ages)

# using builtin enumerate to create a list of tuples -> (index, value)
grades = [6.0, 7.6, 9.8, 10.0]
print(list(enumerate(grades))) # print [(0, 6.0), (1, 7.6), (2, 9.8), (3, 10.0)]
# using builtin range to create a list of indexes
print(list(range(len(grades)))) # print [0, 1, 2, 3]
# iterating 
for tuple in enumerate(grades):
    print(tuple)