d = []
n = int(input())
for _ in range(n):
    input_data = input().split()
    if input_data[0] == "push":
        d.append(input_data[1])

    elif input_data[0] == "pop":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop(-1)

    elif input_data[0] == "size":
        print(len(d))

    elif input_data[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif input_data[0] == "top":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])