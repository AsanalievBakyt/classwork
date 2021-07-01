

# money = 1000
# year = 5
# percent = 10
# i = 0
# while i < year:
#     money += money * 10 // 100
#     print(money)
#     i += 1

# print(help(list))

# l1 = ['ddddddd', 'vv', 'a32', 'qwe', 'asadsadadsda', 'maksim', 'bakyt']
#
# i = 0
#
# while i < len(l1):
#     if len(l1[i]) < 7:
#         print(l1[i])
#     i += 1


L =[1,2,[3,4],[10,2],7,8,9,{'name':'bakyt'}]

for i in L:
    if isinstance(i,(list, dict)):
        print(i)
