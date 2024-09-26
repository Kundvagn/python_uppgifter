from random import random;
# You got 5 shots
# 1 2 3 4 5
# * * * * *
# Shot nr 1 at: 3
# Hit on open target
# 1 2 3 4 5
# * * O * *
# Shot nr 2 at: 1
# Hit on open target
# 1 2 3 4 5
# O * O * *
# Shot nr 3 at: 1
# Miss
# 1 2 3 4 5
# O * O * *
# Shot nr 4 at: 1
# Hit on closed target
# 1 2 3 4 5
# O * O * *
# Shot nr 5 at: 5
# Miss
# 1 2 3 4 5
# O * O * *
# You hit 2 of 5 targets

target_states = 0b00000
def get_target_states() -> str:
    arr = []
    for i in range(0, 5):
        mask = 1 << i
        arr.append("O " if (mask & target_states) else "* ")
    return ''.join(arr)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Biathlon".center(38))
print()
print("a hit or miss game".center(38))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("You got 5 shots")
print("1 2 3 4 5")
print(get_target_states())
for i in range(1, 6):
    target_in = 0

    while True:
        print("shoot nr", i, "at:", end=" ")
        raw_input = input()
        if not raw_input.isdigit():
            print("input a number")
            continue
        if int(raw_input) < 1 or int(raw_input) > 5:
            print("input a number between 1 and 5")
            continue
        target_in = int(raw_input) - 1
        break

    if random() > 0.5:
        print("Miss")
    else:
        if (1 << target_in) & target_states:
            print("Hit on closed target")
        else:
            target_states = (1 << target_in) | target_states
            print("Hit on open target")
    
    print("1 2 3 4 5")
    print(get_target_states())
    print()
    hits = 0
    for i in range(0, 5):
        if (1 << i) & target_states:
            hits += 1
    print(f"You hit {hits} targets")