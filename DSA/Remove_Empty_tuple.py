# using filter function

"""tup = [(1,2,3),(),(1,2),(),(1,2,3,4)]

output=  list(filter(lambda x : len(x)>0, tup))

print(tup)
print(output)
"""
from operator import itemgetter

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


# sorting by multiples keys

"""from operator import itemgetter

d =  [
      {"name": "Nandini", "age": 20},
      {"name": "Manjeet", "age": 20},
      {"name": "Nikhil", "age": 19}
     ]

sorted_dict = sorted(d,key=itemgetter('age','name'))
print(sorted_dict)
"""

"""d =  [
      {"name": "Nandini", "age": 20},
      {"name": "Manjeet", "age": 20},
      {"name": "Nikhil", "age": 19}
     ]
sorted_dict = sorted(d,key=itemgetter('age'),reverse=True)

print(sorted_dict)
"""
"""d =  [
      {"name": "Nandini", "age": 20},
      {"name": "Manjeet", "age": 20},
      {"name": "Nikhil", "age": 19}
     ]
sorted_dict1 = sorted(d,key=lambda key : key['age'])

print(sorted_dict1)
"""

"""d =   [
          {"name": "Nandini", "age": 20},
          {"name": "Manjeet", "age": 20},
          {"name": "Nikhil", "age": 19}
      ]

sorted_dict1 = sorted(d,key= lambda key : (key['name'] ,key['age']))

print(sorted_dict1)
"""

"""dict1 = {"a":1,"b":2}
dict2 = {"c":2,"d":3}

dict1.update(dict2)

print(dict1)
"""
"""
dict1 = {"a":1,"b":2,"c":3,"d":4}
dict2 = {"d":5,"e":6,"f":7,"g":8}

dict3 = dict1.copy()

for key , val in dict2.items():

    dict3[key]=val

print(dict3)"""


# key values pairs into flats dictionary

"""input = [("name","CitiusTech"),("location","Hydrabad"),("Salary",1200)]

dict1 = {}

for tup in input:
    key , val = tup
    dict1[key]=val

print(dict1)


input = [("name","CitiusTech"),("location","Hydrabad"),("Salary",1200)]

dict2 = dict(input)

print(dict2)
"""

##------------------------------------------ Using dictionary comprehension ------------------------------

"""input = [("name","Citiustech"),("age",100),("location","Hydrabad"),("Salary",12000)]

my_dict = {key:val for key,val in input}

print(my_dict)
"""

##--------------------------------------Using zip functions-------------------------------------------------

a = ("name","age","salary")
b = ("CitiusTech",34,1200)

dict1 = dict(zip(a,b))

print(dict1)































