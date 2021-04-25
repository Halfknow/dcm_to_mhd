import os

f = open("./IndexNumber.txt", "a")
for i in range(376):
    zeros = ""
    zero_num = 6 - len(str(i))
    for j in range(zero_num):
        zeros = zeros + "0"
    f.write("./" + zeros + str(i) + ".dcm\n")
f.close()

