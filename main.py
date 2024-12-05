import doctest
import json

doctest.testfile("doctest.txt")
with open("./data/data.json", "r") as jsonFile:
    G = json.load(jsonFile)
print(G["H"])