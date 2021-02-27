# for i in range(3):
#     locals()['part' + str(i)] = i
# print(part0)
# print(part1)
# print(part2)
import os

#
# def Main():
#     for i in range(3):
#         locals()['part'+str(i)] = i
#     print(part0)
#     print(part1)
#     print(part2)
#
# Main()
print(os.path.abspath(os.path.join(os.getcwd(), "..")))