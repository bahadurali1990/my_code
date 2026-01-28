# using filter function

"""tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output=  list(filter(lambda x : len(x)>0, tup))

print(tup)
print(output)
"""

# using list comprehension

tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output = [x for x in tup if len(x)>0]

print(output)


