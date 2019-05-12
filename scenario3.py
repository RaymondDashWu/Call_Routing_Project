# Scenario 3: Multiple long carrier route lists
# You have 5 carrier route lists, each with 10,000,000 (10M) entries (in arbitrary order) and a list of 10,000 phone numbers. How can you speed up your route cost lookup solution to handle this larger dataset?
import time
import glob
import os

start = time.time()
start_read = time.time()
phone_num_cost = {}
cell_number_list = {}


# Importing all routes and associated costs and storing them into memory
# Time Complexity: O(n*m) to iterate through m route cost files with each one containing
# n lines
# Space Complexity: O(n*m) to store all n values of all m route costs files
all_route_costs = glob.glob(os.path.join('', "route-costs-*.txt"))
for route in all_route_costs:
    with open(route, "r") as f:
        for line in f:
            (key, val) = line.strip('\n').split(',')
            phone_num_cost[key] = val

# Importing all the phone numbers we need to find costs for
# Time Complexity: O(n*m) to iterate through m phone number files with each one containing
# n lines
# Space Complexity: O(n*m) to store all n values of all m phone number files
with open("phone-numbers-10000.txt", "r") as f:
    for line in f:
        (key, val) = line.split('\n')
        cell_number_list[key] = val

end_read = time.time()

def search_for_cost(dictionary, number):
    """Searches for the given phone number and returns associated cost
    Format ex: +1200, .03
    Time Complexity: O(m) where m is the length of the phone number
    Space Complexity: O(l) to store the length of the phone number. Decreases until
    a match is found"""
    prefix = number
    min_prefix_len = 1
    while len(prefix) > min_prefix_len:
        if prefix in dictionary: # O(m) where m is len(phone_num) iterations
            # TODO: Find lowest price for numbers
            result = '{}, {}\n'.format(number, dictionary[prefix])
            return result # O(l)
        else:
           prefix = prefix[:-1]
    if prefix not in dictionary:
        return '{}, {}\n'.format(number, 0)

def anotate_data(phone_num_list, dictionary):
    """Writes the phone number and associated cost to a file
    Time Complexity: O(n) to iterate through all keys in phone_num_list dictionary
    Space Complexity: O(1) this function does not store anything in memory."""
    file = open('route-costs-3.txt', 'w+')
    for number in phone_num_list.keys():
        data_cost = search_for_cost(dictionary, number)
        # print('cost data => ', data_cost)
        if data_cost is not None:
            file.write(data_cost)
    file.close()

def main():
    print(anotate_data(cell_number_list, phone_num_cost))
    end = time.time()
    print(end-start)
    print("time to read:", end_read - start_read)

if __name__ == "__main__":
    main()
