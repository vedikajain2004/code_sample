'''The following problem seeks to solve the two sat problem. Although it is NP complete, yet it can be solved for some cases. This program seeks to solve the problem for small cases (upto 10,000 variables).'''
import math
import random
# loading the file contents
with open('C:/Users/user/Downloads/stanford-algs-master/stanford-algs-master/testCases/course4/assignment4TwoSat/output_beaunus_31_10000.txt') as f:
    r = f.readlines()
# some required initialisations
n, conditions, ans = int(r.pop(0)), {}, 0
vals, s = [None] * n, set()
# reading the conditions
for e in r:
    conditions[(int(e.split()[0]), int(e.split()[1]))] = 0
# Reduction of The Problem: If a variable occurs only as its affirmation or negation in all the conditions, then it can be assigned the proper value to hold that condition true. This reduces our problem size. If we do this iteratively, we can reduce the number of conditions and variables drastically.
old_len, new_len = len(conditions), 0
while old_len != new_len:
    s = set()
    for y in conditions:
        s.add(y[0])
        s.add(y[1])
    old_len = len(s)
    for p in list(s):
        if -p not in s:
            for t in set(conditions.keys()):
                if p in t:
                    conditions.pop(t)
            s.remove(p)
            if p < 0:
                vals[-p-1] = 0
            else:
                vals[p-1] = 1
    new_len = len(s)
# final problem size
print(len(conditions), len(s))
if not len(conditions): #if all the conditions have been already satisfied, we can stop here
    ans = 1
    print(ans)
else:
    for i in range(int(math.log2(len(s)))):
        for u in range(n):
            if u + 1 in s or vals[u] is None:
                vals[u] = random.choice((0, 1))
        for j in range(2 * len(s) ** 2):
            for k in conditions:
                if (k[0] < 0 and vals[-k[0] - 1] == 0) or (k[0] > 0 and vals[k[0] - 1] == 1) or (k[1] < 0 and vals[-k[1] - 1] == 0) or (k[1] > 0 and vals[k[1] - 1] == 1):
                    conditions[k] = 1
                else:
                    conditions[k] = 0
            if sum(conditions.values()) != len(conditions):
                m = random.choice([d for d in conditions if conditions[d] == 0])
                g = random.choice(m)
                if g > 0:
                    if vals[g-1] == 0:
                        vals[g-1] = 1
                    else:
                        vals[g-1] = 0
                else:
                    if vals[-g-1] == 0:
                        vals[-g-1] = 1
                    else:
                        vals[-g-1] = 0
            else:
                ans = 1
                print(ans)
                break
        if ans:
            break
    else:
        print(ans)
