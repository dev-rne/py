# def reportFun (max_and_min, dataArr):
#     max = max_and_min[1]
#     min = max_and_min[0]

#     for i in dataArr:
#         if i >= min and i <= max:
#             print("Nothing to report")
#         elif i == -999:
#             break
#         else:
#             print("Alert!")
#             break

# a = [10, 20]
# b = [15, 10 ,20, 0 ,15 ,-999]

# reportFun(a,b)

L = input().split()
min = int(L[0])
max = int(L[1])

temp = int(input())

while temp != -999:
    if min <= temp <= max:
        print("Nothing to report!")
        temp = int(input())
    else:
        print("Alert!")
        break