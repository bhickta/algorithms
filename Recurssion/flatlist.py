from typing import Iterable
question = [2, {4, 5, 8}, [3, [3, [3]], 6], 1, "ssd"]

def flatlist(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            result.extend(flatlist(item))
        else:
            result.append(item)
    return result

flatlist = flatlist(question)
print(flatlist)