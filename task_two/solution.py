def extract_type(text, searched_type):
    extract = lambda symbol, repeats: str(symbol) * repeats
    match_type = lambda symbol: type(symbol) is searched_type

    finds = [extract(pair[0], pair[1]) for pair in text if match_type(pair[0])]
    return ''.join(finds)


def reversed_dict(dikt):
    return  {value:key for key, value in dikt.items()}


def flatten_dict(dikt, key=None):
    flattened = {}
    for top_key, top_value in dikt.items():
        if type(top_value) is dict:
            inner_dict = flatten_dict(top_value, top_key)
            for inner_key, inner_value in inner_dict.items():
                flattened[top_key + "." + inner_key] = inner_value
        else:
            flattened[top_key] = top_value
    return flattened


def unflatten_dict(dikt):
    unflattened = {}
    for top_key, top_value in dikt.items():
        keys = top_key.split('.')
        outer_list = unflattened
        for inner_key in keys:
            if inner_key not in outer_list.keys():
                outer_list[inner_key] = {}
            if inner_key == keys[-1]:
                outer_list[inner_key] = top_value
            outer_list = outer_list[inner_key]
    return unflattened


def reps(collection):
    return tuple([item for item in collection if collection.count(item) != 1])
