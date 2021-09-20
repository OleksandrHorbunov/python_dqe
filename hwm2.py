# Import module random
import random
import string

# create a list of random number of dicts (from 2 to 10)
def get_dicts(number_dicts):
    dict_list = []                                              # Create empty list
    for i in range(number_dicts):                               # Go through the list of dicts
        number = random.randint(1, number_dicts)                # number of keys and values in a dict
        keys = random.sample(string.ascii_lowercase, number)    # random numbers of keys (letter)
        values = random.sample(range(0, 100), number)           # random numbers of values (number)
        dictionary = dict(zip(keys, values))                    # create dictionary
        dict_list.append(dictionary)                            # add dict to list
    print("List of dicts\n", dict_list)                                            # list of dicts
    return dict_list                                            # function returns a list


# create one common dict
def get_common_dict(dicts):
    res = {}                                               # final dict
    res1 = {}                                              # auxiliary dict to keep key and dict num
    dn = 1                                                 # dict counter
    for dic in dicts:                                      # go through list of dicts
        for key in dic.keys():                             # for each key in dict
            if key not in res.keys():                      # if key is not in final dict
                res[key] = dic[key]                        # add key to final dict
            if key in res.keys() and \
                    dic[key] > res[key]:                   # if key value in final dict less then the same from another
                res[key] = dic[key]                        # change value in final dict for key
                res1[key] = dn                             # add key: dn to auxiliary dict to know key and dict number
            elif key in res.keys() and \
                    dic[key] < res[key]:                   # if key value in final dict more then the same from another
                res1[key] = dn                             # change value for key
        dn += 1                                            # increase counter
    print("Common dict with the biggest value for key\n",
          res)                                             # Print common dict
    print("Auxiliary dict\n", res1)                        # Print auxiliary dict

    for k in res1.keys():                                  # Go through auxiliary dict
        new_key = k + "_" + str(res1[k])                   # Create a new key
        res[new_key] = res.pop(k)                          # Create a new key in final dict with value
    print("Final dict with new keys\n", res)               # Print final dict with updated keys


if __name__ == "__main__":
    # Generate random number of dicts
    number_dicts = random.randint(2, 10)                   # Generate number of dicts
    g_dict_list = get_dicts(number_dicts)                  # Call get_dicts
    get_common_dict(g_dict_list)                           # Call get_common_dict
