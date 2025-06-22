def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result  = {}
    for group in numbers:
            result.setdefault(group['group'], []).append(group['number'])
    return result



numbers = [
    {"number": 2,
     "group": 1
     },
    {"number": 2,
     "group": 5
    },
    {"number": 2,
     "group": 3
    },
    {"number": 2,
     "group": 1
     },
    {"number": 2,
     "group": 5
    },
    {"number": 2,
     "group": 3
    },
]

result=group_indices(numbers)
print(result)