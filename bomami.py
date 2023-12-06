lst = [11, 13, 19, 20]
# ans = [0]*10

for i in range(1, len(lst)):
    diff = lst[i] - lst[i - 1]
    while diff > 1:
        print(lst[i] - diff + 1)
        diff -=1

# for i in range(0, len(lst)):
#     idx = lst[i] % 10 - 1
#     ans[idx] = lst[i]

# for i in range(0, len(ans)):
#     if ans[i] == 0:
#         print(i+10+1)