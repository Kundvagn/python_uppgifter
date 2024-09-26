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

n = 1
print("      ", flippblipp(n))
while(True):
    n += 1
    print("nästa: ", end="")
    i = input()
    if i != flippblipp(n):
        print("Game Over")
        break