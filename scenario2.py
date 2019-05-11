# Scenario 2: List of route costs to check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
import time
start = time.time()
phone_num_cost = {}

with open("route-costs-100000.txt", "r") as f:
    for line in f:
        (key, val) = line.strip('\n').split(',')
        phone_num_cost[key] = val

with open("phone-numbers-1000.txt", "r") as f:
    phone_num = f.read().split()


def search_for_cost(dictionary, number):
    prefix = number
    min_prefix_len = 1
    while len(prefix) > min_prefix_len:

        if prefix in dictionary: # O(m) where m is len(phone_num) iterations
            # print('number : {}, value: {}'.format(number, dictionary[prefix]))
            result = '{}, {}\n'.format(number, dictionary[prefix])
            return result # O(l)
        # if prefix not in dictionary:
        #     raise ValueError('not found')
        else:
           prefix = prefix[:-1]


def anotate_data(phone_num_list, dictionary):
    file = open('route-costs-2.txt', 'w+')
    for number in phone_num_list:
        data_cost = search_for_cost(dictionary, number)
        # print('cost data => ', data_cost)
        if data_cost is not None:
            file.write(data_cost)
    file.close()



def main():


    print(anotate_data(phone_num, phone_num_cost))
    end = time.time()
    print(end-start)

if __name__ == "__main__":
    main()
