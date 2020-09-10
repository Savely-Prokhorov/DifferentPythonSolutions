groups = [67687, 667566, 4553334, 6566, 4332, 87886, 12321]
groups.sort()

groups_to_win = len(groups) // 2 + 1

res = 0
for i in range(groups_to_win):
    res += groups[i] // 2 + 1

print(res)
