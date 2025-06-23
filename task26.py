def merge_dicts(a: dict, b: dict) -> dict:
    result = {}
    result.update(a)
    result.update(b)

    return result
a = {
    'a': 1,
    'b': 2
}
b = {
    'b': 5,
    'c': 3
}

result = def merge_dicts(a,b)