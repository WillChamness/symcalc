def print_menu():
    """Prints a menu to the screen and prompts for an input.
    """
    user_input = ""
    MIN = 1
    MAX = 3
    menu = """(1) exit
    \r(2) y=
    \r(3) algebra"""
    print(menu)
    while not __valid_input__(user_input, MIN, MAX):
        user_input = input(">>> ")
    

def __valid_input__(user_input, min, max):
    """Determines whether the input is valid or not.
    """
    try:
        return min <= int(user_input) and int(user_input) <= max
    except ValueError:
        return False



try:
    import sympy
except ModuleNotFoundError:
    print("Error using sympy. Please install with the following command:\n")
    print("pip install sympy")
    exit()

print_menu()