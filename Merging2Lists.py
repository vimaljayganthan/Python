l1 = [7, 2, 1, 2]
l2 = [1, 3, 2, 6]

for i in l2:
    if i not in l1:
        l1.append(i)

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print(l1)




# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 5, 7, 8, 10]

# i = 0
# j = 0
# res = []

# while i < len(l1) and j < len(l2):
#     if l1[i] < l2[j]:
#         if l1[i] not in res:
#             res.append(l1[i])
#         i += 1
#     elif l1[i] > l2[j]:
#         if l2[j] not in res:
#             res.append(l2[j])
#         j += 1
#     else:
#         if l1[i] not in res:
#             res.append(l1[i])
#         i += 1
#         j += 1

# while i < len(l1):
#     if l1[i] not in res:
#         res.append(l1[i])
#     i += 1

# while j < len(l2):
#     if l2[j] not in res:
#         res.append(l2[j])
#     j += 1

# print(res)