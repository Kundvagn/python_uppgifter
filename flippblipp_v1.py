n = 30
new_list = [None]*(n - 1)

for i in range(1, n):
    new_list[i - 1] = (str(i) + '\n' if i%5 else "blipp\n") if i%3 else ("flipp\n" if i%5 else "flipp blipp\n")
new_string = ''.join(new_list)
