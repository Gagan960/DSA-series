# for i in range(1,5):
#     for j in range(i):
#         print("*",end='')
#     print()
    

# # OUTPUT *
# #        **
# #        ***
# #        ****
# #        *****

# for i in range(1,5):
#     for j in range(i):
#         print(i,end='')
#     print()

# # OUTPUT 1
# #        22
# #        333
# #        4444
# a=65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(a),end='')
#     print()
#     a=a+1

# # A
# # BB
# # CCC
# # DDDD

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# # 1
# # 12
# # 123
# # 1234

# # REVERSE TRIANGLE

# for i in range(0,5):
#     for j in range(i+1,0,-1):
#         print(j,end='')
#     print()

# # 1
# # 21
# # 321
# # 4321
# # 54321

# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end='')
#         num=num+1
#     print()
# # 1
# # 23
# # 456
# # 78910

# for i in range(1,5):
#     for j in range(1,i):
#         print(" ",end="")
#     for j in range(0,5-i,1):
#         print(i,end="")
#     print()

# 1111
#  222
#   33
#    4

#PYRAMID PATTERN
# for i in range(0,5):
#     for j in range(0,4-i,1):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print()

#    1
#   121
#  12321
# 1234321

for i in range(1,5):
    for j in range(4-i,0,-1):
        print(" ",end='')
    print("*",end='')
    if i>1:   
        for k in range(2,i+1):
          print(" ",end=" ")
        print("*",end='')
    print()
for i in range(1,4):
    for j in range(0,i):
        print(" ",end="")
    print("*",end="")
    for j in range(4-i,1,-1):
        print(" ",end=" ")
    if i<3:
        print("*",end="")
    print()
    