numbers = ["一","二","三","四","五","六","七","八","九"]
for i in range(1,10):
    for j in range(1,10):
        if i * j >=10:
            space = " "
        else:
            space = "  "
        print(numbers[i-1] + numbers[j-1] + "得%d" %  (i * j),end = space)
    print()
