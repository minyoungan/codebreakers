# sample_input = {
#     "a":1,"b":2,"c":3,"d":3
# }

# sample_output = [
#     {"a":1,"b":2,"c":3},
#     {"a":1,"b",2,"d":3}
# ]

# I am going to copy this example and change a bit

# sample_input = {
#     "a":1,"b":2,"c":3,"d":3,"e":3 # Is this a valid input?
# }

# sample_output = [
#     {"a":1,"b":2,"c":3},
#     {"a":1,"b",2,"d":3},
#     {"a":1,"b",2,"e":3}
# ]

# sample_input = {
#     "a":1,"b":2,"c":3,"d":3,"e":3,"f":2

# sample_output = [
#     {"a":1,"b":2,"c":3},
#     {"a":1,"b",2,"d":3},
#     {"a":1,"f",2,"e":3}
# ]

# my approach would be build a new dictionary 
# counter is key and alphabet is value.
# while iterating the given input, if counter doesn't exist add the alphbet
# # if exists continue 
# Time O(N) and Space O(N)

# Are things looking good?
# Should I alter the given dictionary or make a copy of it?
# Does that sound good? Should we start code?

def unique_value(input_dict):
    reversed_dict = {}
    ans = {}

    for alphabet in input_dict:
        if input_dict[alphabet] in reversed_dict:
            continue
        else:
            reversed_dict[input_dict[alphabet]] = alphabet
    
    for counter in reversed_dict:
        ans[reversed_dict[counter]] = counter
    
    return ans # TODO

print(unique_value({"a":1,"b":2,"c":3,"d":3}))


def foobar(input_dict):
    new_dict = {}
    seen = set()
    for key, val in input_dict.items():
        if val not in seen:
            new_dict[key] = val
            seen.add(val)
    return new_dict

print(foobar({"a":1,"b":2,"c":3,"d":3}))
