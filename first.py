def get_os_info():
    try:
        with open('/etc/os-release', 'r') as os_release_file:
            os_info = {}
            for line in os_release_file:
                key, value = line.strip().split('=', 1)
                os_info[key] = value.strip('"')
            return os_info
    except FileNotFoundError:
        return None


def greet_and_welcome(name):
    print(f"Hello {name}!")

    os_info = get_os_info()
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
