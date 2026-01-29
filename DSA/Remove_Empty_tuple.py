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

# using list comprehension

"""dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}

total_sum = sum([value for value in dict1.values()])

print(total_sum)
"""

"""dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}
sum = 0
for val in dict1.values():
    sum=sum+val
print(sum)
"""

# with the help of map and lambda

"""dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}

output = sum(list(map(lambda key : dict1[key],dict1)))

print(output)"""

"""dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}

final_output = dict1.pop("a")

print(final_output)
"""

"""dict1 = {"a":1,"b":2,"c":3,"d":4,"e":5}

dict2 = dict1.popitem()

print(dict2)
print(dict1)
"""

"""from operator import itemgetter

d = [
      {"name": "Nandini", "age": 20},
      {"name": "Manjeet", "age": 20},
      {"name": "Nikhil", "age": 19}
    ]

print(f"sorted of list of dict {sorted(d,key=itemgetter('age'))}")
"""









