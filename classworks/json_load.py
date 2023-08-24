import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "r") as write_file:
    r=json.load(write_file)
    print(r)
    print(type(r))