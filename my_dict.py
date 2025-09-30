#to get key value of age
my_dict = {"name":"kryssie", "age":70}
key = "age"
if key in my_dict:
    value = my_dict[key]
print(value)
#to get keys only
my_dict = {"name":"kryssie", "age":70, "city":"jos"}
key = [k for k in my_dict]
print(key)
#to get values
my_dict = {"name":"kryssie", "age":70, "city":"jos"}
values = [my_dict[k] for k in my_dict]
print(values)
#key value pairs
my_dict = {"name":"kryssie", "age":70, "city":"jos"}
items = []
for k in my_dict:
    items += [(k, my_dict[k])]
print(items)
#how to update a value
my_dict = {"name":"kryssie", "age":70, "city":"jos"}
my_dict["age"] = 20
my_dict["city"] = "mangu"
print(my_dict)
my_dict = {"name":"kryssie", "age":70, "city":"jos"}
key = "age"
value = my_dict[key] 
if key in my_dict:
    del my_dict[key]
print(my_dict)
