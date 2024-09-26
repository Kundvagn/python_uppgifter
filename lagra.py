
login_dict: dict = {
    "johannes": "kalat",
    }
storage_dict: dict = {}
profile: str = None

help_string = """h - get this text
    q - quit
    l - login
    if logged in:
    add - add a new item to your storage
    look - check all items in storage
"""

print(help_string)
while True:
    raw_input = input("$ ").split(" ")
    if len(raw_input) == 0:
        continue
    match(raw_input[0]):
        case 'q':
            break

        case 'l':
            if profile:
                print(f"Logged in as: {profile}")
                continue

            username = input("username: ")
            password = input("password: ")
            if login_dict.get(username) != password:
                print("Invalid Login")
                continue

            print("Successfully logged in")
            profile = username
            if not profile in storage_dict:
                storage_dict[profile] = []

        case "add":
            if not profile:
                print("not logged in")
                continue
            item: str = None
            if len(raw_input) > 1:
                item = raw_input[1]
            else:
                item = input("item: ")
            storage_dict[profile].append(item)
            print(f"added {item}")
            
        case "look":
            if not profile:
                print("not logged in")
                continue
            print(f"{profile}'s storage:")
            if len(storage_dict[profile]) == 0:
                print("you are poor!")
            for i in storage_dict[profile]:
                print(f"{i},")
            print()
        case _:
            print(help_string)