import platform


def check_os():
    system = platform.system()


def greet_and_welcome(name):
    print(f"Hello {name}!")

    os_info = check_os()
    if os_info:
        os_name = os_info.get('PRETTY_NAME', 'Linux')
        print(f"Welcome to {os_name}, {name}!")
    else:
        print("Unable to retrieve OS information.")


if __name__ == "__main__":
    # Get user input for name
    user_name = input("Enter your name: ")

    # Call the greet_and_welcome function
    greet_and_welcome(user_name)

# chat gpt lesgooo
