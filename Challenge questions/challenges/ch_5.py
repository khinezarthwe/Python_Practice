# Challenge:5
#Given Strings of code equations like, "45 >= 67 56==70 30 <= 78" and output should be binary "0 0 1"
# { input is seprated with space and output should be on new line}

import re
input = "45>=67 56==70 30<=78"
expected = []
input_list = input.split(" ")
for value in input_list:
    res = re.match("([0-9]+)([\+=<>]+)([0-9]+)", value)
    if res is not None:
        if res.group(2) == "==":
            expected.append(1 if int(res.group(1)) == int(res.group(3)) else 0)
        elif res.group(2) == ">=":
            expected.append(1 if int(res.group(1)) >= int(res.group(3)) else 0)
        elif res.group(2) == "<=":
            expected.append(1 if int(res.group(1)) <= int(res.group(3)) else 0)
        elif res.group(2) == "<":
            expected.append(1 if int(res.group(1)) < int(res.group(3)) else 0)
        elif res.group(2) == ">":
            expected.append(1 if int(res.group(1)) > int(res.group(3)) else 0)
        else:
            print("operation error")

print(expected)
