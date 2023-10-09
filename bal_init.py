import json

balance = {
    "Vincent": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Leo": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Jeffery": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Saarukan": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Zion": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Yousif": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
    "Ali": {
        "Bal1": 0,
        "Bal2": 0,
        "Bal3": 0,
        "Bal4": 0,
        "Bal5": 0,
        "Bal6": 0,
    },
}

with open('balances.json', 'w') as json_file:
    json.dump(balance, json_file, indent=4)
