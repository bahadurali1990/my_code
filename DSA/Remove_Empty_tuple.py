tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output=  list(map(lambda x : x if len(x)>0 else None, tup))

print(tup)
print(output)

