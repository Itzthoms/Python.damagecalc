

i = 10
while i in range(10):
    print("Iteration:", i)


i = 8
while i < 16:
    print("Iteration:", i)
    i += 1


i = 1
k = 2
while i < 10:
    print(i, ":", k)
    k *= 2
    i += 1

for i in range(10):
    for j in range(10):
        print(i*j)
    print("---")
    