

    
list = [1,2,3,4,5,1,2,6]
target = 2

for i in list:
    for j in list:
        for k in list:
            count = i + j + k
            if (count == target):
                print(i, "+", j, "+", k, "this sum is equal to", target, "which is", count)
                break   