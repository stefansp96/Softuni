parking_users = {}
entries = int(input())

for entry in range(entries):
    current_user = input().split()
    action = current_user[0]
    username = current_user[1]

    if action == 'register':
        license_plate = current_user[2]
        if username in parking_users.keys():
            print(f"ERROR: already registered with plate number {parking_users[username]}")
        else:
            parking_users[username] = license_plate
            print(f"{username} registered {parking_users[username]} successfully")
    elif action == 'unregister':
        if username not in parking_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_users[username]

for user, license_plate in parking_users.items():
    print(f"{user} => {license_plate}")
