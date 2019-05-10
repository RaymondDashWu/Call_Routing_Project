# Scenario 1: One-time route cost check

# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?

with open("route-costs-106000.txt", "r") as f:
    words = f.read().split("\n")



def search_for_cost():
    route_num = {'+86153':'0.84', '+449275049':'0.49', '+8130':'0.68'}
    phone_num = '+81301234567'
    is_match = False
    # counter = 0
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
