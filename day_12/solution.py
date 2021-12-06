import re
import json
f = open("input.txt").read().strip()
# f = open("testInput.txt").read().strip()

a = re.findall("-*\d+", f)

print("part 1", sum((int(x) for x in a)))

asdf = json.loads(f)

c = 0

def dfs(node):
    currC = 0
    if type(node) is list:
        for elem in node:
            currC += dfs(elem)
            # print(currC)
    elif type(node) is dict:
        foundRed = False
        for value in node.values():
            print(value, list(node.values()))
            # if value != "red" and :
            #     foundRed = True
        if foundRed:
            print(type(node.values()))
            print(str(node.values()))
        if not foundRed:
            for k, v in node.items():
                if k != "red:":
                    currC += dfs(v)
    elif str(node).isnumeric():
        return int(node)
    return currC


print("part 2", dfs(asdf))
