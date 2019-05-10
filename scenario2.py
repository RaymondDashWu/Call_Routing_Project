# Scenario 2: List of route costs to check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?


# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?
phone_num_cost = {}
with open("route-costs-100.txt", "r") as f:
    for line in f:
        (key, val) = line.strip(',')
        phone_num_cost[int(key)] = val




def search_for_cost(dictionary, ):

    is_match = False
    prefix = phone_num
    min_prefix_len = 1

# 8130 compared to 81201234567

while len(prefix) > min_prefix_len:  # O(m) where m is len(phone_num) iterations
   if prefix in route_num:  # O(l)
       print(phone_num, route_num[prefix])
       break
   else:
       # counter = len(phone_num) - 1
       prefix = prefix[:-1]


# Provide full  phone # with route



    # """return the index of item in sorted array or None if item is not found"""
    # # implement binary_search_iterative and binary_search_recursive below, then
    # # change this to call your implementation to verify it passes all tests
    # array.sort()
    # # return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)
