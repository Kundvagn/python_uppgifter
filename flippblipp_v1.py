n = 30

for i in range(1, n):
    if i % 3:
        if i % 5:
            print(i)
        else:
            print("blipp")
    elif i % 5:
        print("flipp")
    else:
        print("flipp blipp")