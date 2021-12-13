import re
import json
f = open("input.txt").read().strip()
# f = open("testInput.txt").read().strip()

a = re.findall("-*\d+", f)

print("part 1", sum((int(x) for x in a)))

asdf = json.loads(f)

c = 0

def dfs(node):
    if type(node) == int:
        return node
    if type(node) == list:
        return sum([dfs(x) for x in node])
    if type(node) != dict:
        return 0
    if "red" in node.values():
        return 0
    else:
        return dfs(list(node.values()))

print("part 2", dfs(asdf))
