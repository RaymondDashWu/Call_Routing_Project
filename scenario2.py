# Scenario 2: List of route costs to check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
import time

start = time.time()
start_read = time.time()
phone_num_cost = {}
cell_number_list = {}

with open("route-costs-106000.txt", "r") as f:
    for line in f:
        (key, val) = line.strip('\n').split(',')
        phone_num_cost[key] = val

with open("phone-numbers-1000.txt", "r") as f:
    for line in f:
        (key, val) = line.split('\n')
        cell_number_list[key] = val

end_read = time.time()

def search_for_cost(dictionary, number):
    prefix = number
    min_prefix_len = 1
    while len(prefix) > min_prefix_len:
        if prefix in dictionary: # O(m) where m is len(phone_num) iterations
            result = '{}, {}\n'.format(number, dictionary[prefix])
            return result # O(l)
        # if prefix not in dictionary:
        #     return '{}, {}\n'.format(number, 0)
        else:
           prefix = prefix[:-1]
    if prefix not in dictionary:
        return '{}, {}\n'.format(number, 0)

def anotate_data(phone_num_list, dictionary):
    file = open('route-costs-2.txt', 'w+')
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
