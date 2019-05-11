# Scenario 2: List of route costs to check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?


phone_num_cost = {}

with open("route-costs-100.txt", "r") as f:
    for line in f:
        (key, val) = line.strip('\n').split(',')
        phone_num_cost[key] = val

with open("phone-numbers-100.txt", "r") as f:
    phone_num = f.read().split()


def search_for_cost(dictionary, phone_num):

    prefix = phone_num
    min_prefix_len = 1
    while len(prefix) > min_prefix_len:

        if prefix in dictionary: # O(m) where m is len(phone_num) iterations
            return (phone_num, dictionary[prefix]) # O(l)
        else:
           prefix = prefix[:-1]


def anotate_data(phone_num_list, dictionary):
    f = open('route-costs-2.txt', 'w+')
    for number in phone_num_list:
        data_cost = search_for_cost(dictionary, number)
        if data_cost is not None:
            f.write(data_cost)
    f.close()



def main():
    print(anotate_data(phone_num, phone_num_cost))



if __name__ == "__main__":
    main()
