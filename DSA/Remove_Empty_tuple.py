# using filter function

"""tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output=  list(filter(lambda x : len(x)>0, tup))

print(tup)
print(output)
"""

# using list comprehension

"""tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output = [x for x in tup if len(x)>0]

print(output)
"""

"""d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
final_out = list(set(sum(d.values(),[])))

print(final_out)
"""

"""dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}

total_sum = sum(dict1.values())

print(total_sum)
"""




