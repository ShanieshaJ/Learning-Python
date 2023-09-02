# list container
value_container = [100, 250, 360, 430, 540, 670, 900]
print("Original list container: ", value_container)
print(type(value_container))
sum_of_items = sum(value_container)
print("Sum of items in container: ", sum_of_items)


# dictionary container
def dict_sum(value_container):
    num_of_items = 0
    for i in value_container:
        num_of_items = num_of_items + value_container[i]
    return num_of_items


value_container = {"a": 100, "b": 250, "c": 360, "d": 430, "e": 540, "f": 670, "g": 900}
print("Original dictionary container: ", value_container)
print(type(value_container))
print("Sum of items in container: ", dict_sum(value_container))

# set container
value_container = {100, 250, 360, 430, 540, 670, 900}
print("Original set container: ", value_container)
print(type(value_container))
set_of_items = sum(value_container)
print("Sum of items in container: ", str(set_of_items))

# tuple container
value_container = (100, 250, 360, 430, 540, 670, 900)
print("Original tuple container: ", value_container)
print(type(value_container))
tuple_of_items = sum(value_container)
print("Sum of items in container: ", tuple_of_items)
