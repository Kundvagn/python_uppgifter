import time;

t = time.time_ns()
n = 3000

new_string = ''.join([(str(i) + '\n' if i%5 else "blipp\n") if i%3 else ("flipp\n" if i%5 else "flipp blipp\n") for i in range(1, n)])

#print(new_string)
nano_time = (time.time_ns() - t)/n
print("n =", f"{n:,d}", ":", round(nano_time, 2), "ns")

