from main import read_file
from main import write_file
from main import check_credentials


def main():
    tries = True

    print("""
    Hi, welcome to the page.
    Please, select an option
    
    1.-See users
    2.-Create a user
    3.-Log in""")

    while tries:
        try:
            option = int(input())

            if type(option) is int:
                if option == 1:
                    read_file()
                    tries = False
                if option == 2:
                    user = input("What is your username?")
                    password = input("Enter your password")

                    credentials = {"user": user, "password": password}
                    write_file(credentials)
                    tries = False
                if option == 3:
                    user = input("What is your username?")
                    password = input("Enter your password")

                    credentials = {"user": user, "password": password}
                    check_credentials(credentials)
                    tries = False
            else:
                print("Invalid option")

        except ValueError:
            print("Enter a valid option")


main()

