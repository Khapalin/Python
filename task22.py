"""

"""


new_var = set(map(int, var2.split()))
new_var2 = set(map(int, var3.split()))
new_var3 = sorted(new_var.intersection(new_var2))
for i in new_var3:
    print(i, end=' ')