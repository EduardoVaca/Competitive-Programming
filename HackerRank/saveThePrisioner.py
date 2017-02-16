tests = int(input())
prisioners, sweets, id_start = [int(x) for x in input().strip().split(' ')]
if id_start + sweets - 1 <= prisioners:
    print(id_start + sweets - 1)
else:
    res = (sweets + id_start - 1) % prisioners
    if res == 0:
        print(prisioners)
    else:
        print(res)
