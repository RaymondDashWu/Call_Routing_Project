# Scenario 2: List of route costs to check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?


# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?
phone_num_cost = {}
with open("route-costs-100.txt", "r") as f:
    for line in f:
        (key, val) = line.strip('\n').split(',')
        phone_num_cost[key] = val



def search_for_cost(dictionary, phone_num):

    prefix = phone_num
    min_prefix_len = 1

    while len(prefix) > min_prefix_len:

        if prefix in dictionary: # O(m) where m is len(phone_num) iterations
            return (phone_num, dictionary[prefix]) # O(l)
        else:
           prefix = prefix[:-1]

def main():
    phone_num = '+449916707'
    print(search_for_cost(phone_num_cost, phone_num))




if __name__ == "__main__":
    main()
    
