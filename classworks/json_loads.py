import json
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian"
   }
}
"""


r=json.loads(json_string)
print(r)
print(type(r))
print(r['researcher']['name'])