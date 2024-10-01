n = 300

def flippblipp(n):
    if n % 3:
        if n % 5:
            return str(n)
        else:
            return "blipp"
    elif n % 5:
        return "flipp"
    else:
        return "flipp blipp"

for i in range(1, n):
    print(flippblipp(i))