import random
import string


def get_dicts(number_dicts):
    # Return a list of random number of dicts (from 2 to 10)

    # Parametrs:
    #   number_dicts (int):  random number of dicts in a list
    dict_list = []
    for i in range(number_dicts):
        number = random.randint(1, 26)            # Dict size
        key_list = []
        key_counter = 0
        while key_counter < number:                         # Check for letter duplicates
            keys = random.choice(string.ascii_lowercase)
            if keys not in key_list:
                key_list.append(keys)
                key_counter += 1
        value_list = []
        value_counter = 0
        while value_counter < number:                          # Check for number duplicates
            values = random.randint(0, 100)
            if values not in value_list:
                value_list.append(values)
                value_counter += 1
        dictionary = dict(zip(key_list, value_list))            # Creating a dict
        dict_list.append(dictionary)                            # Adding a dict to a list
    #print("List of dicts\n", dict_list)
    return dict_list


# create one common dict
def get_common_dict(dicts):
    # Return one common dict

    # Parametrs:
    #   dicts (list): get generated list of dicts
    res = {}
    dict_aux = {}       # Creating auxiliary dict to keep key and num of dict
    for dict_order in range(len(dicts)):        # Go through the list of dicts
        for dict_key in dicts[dict_order]:
            if dict_key not in res:
                res[dict_key] = dicts[dict_order][dict_key]     # Adding dict elen to res dict
                for sub_dict_order in range(dict_order + 1, len(dicts)):        # Checking for the max key value
                    if dict_key in dicts[sub_dict_order] and \
                            dicts[sub_dict_order][dict_key] > dicts[dict_order][dict_key]:
                        res[dict_key] = dicts[sub_dict_order][dict_key]         # Changing the value
                        dict_aux[dict_key] = sub_dict_order + 1                 # Adding key and dict number
                    elif dict_key in dicts[sub_dict_order] and \
                            dicts[sub_dict_order][dict_key] < dicts[dict_order][dict_key]:
                        dict_aux[dict_key] = dict_order + 1
    print("Auxiliary dict\n", dict_aux)
    for aux_key in dict_aux.keys():     # Changing key to new key with suffix of dict number
        new_key = aux_key + "_" + str(dict_aux[aux_key])
        res[new_key] = res.pop(aux_key)
    #print("Common dict\n", res)
    return res


if __name__ == "__main__":
    # Generate random number of dicts
    number_dicts = random.randint(2, 10)
    g_dict_list = get_dicts(number_dicts)
    g_dict_common = get_common_dict(g_dict_list)
    print("List of dicts\n", g_dict_list)
    print("Common dict\n", g_dict_common)

