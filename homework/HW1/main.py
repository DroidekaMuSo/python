import json

def read_file():
    with open("data.json", "r") as file:
        read_data = json.load(file)

        for user in read_data["users"]:
            print("User:", user["user"])
            print("Password:", user["password"])


def write_file(user):
    with open("data.json", "r+") as file:
        data = json.load(file)
        user["id"] = len(data["users"])+1

        data["users"].append(user)

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        print(f"User created, welcome {user["user"]}")


def check_credentials(user):
    with open("data.json", "r") as file:
        login = False
        data = json.load(file)

        for credentials in data["users"]:
            if credentials["user"] == user["user"] and credentials["password"] == user["password"]:
                login = True
                break

        if login:
            print(f"Welcome {user["user"]}")
        else:
            print("Credentials don't match")


