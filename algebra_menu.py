import algebra
from sympy import sympify, SympifyError
import os

def print_menu():
    """Defines the menu the user will be presented. Returns
    the users choice.
    """
    MIN = 1
    MAX = 5
    menu = """(1) back
    \r(2) factor
    \r(3) expand
    \r(4) zeros
    \r(5) solve""" 
    user_input = ""

    print(menu)
    while not __valid_input__(user_input, MIN, MAX):
        user_input = input(">>> ")
    
    return user_input


def __valid_input__(user_input, min, max):
    """Determines whether the input is valid or not.
    """
    try:
        return min <= int(user_input) and int(user_input) <= max
    except ValueError:
        return False


def goto_function(choice):
    """Returns the result of the user's choice and expressions.
    """
    switch = {
        2: factor_prompt()
    }
    input("\nPress enter to continue.")
    os.system("cls || clear")
    return switch.get(choice, None)


def prompt_single():
    """Returns a sympified verison of the user's input, if possible.
    """
    try:
        print("Expression (ctrl-c to go back):")
        return sympify(input(">>> "))
    except SympifyError:
        print("Unable to parse expression. Returning...")
    except:
        print("Returning...")


def factor_prompt():
    """Defines prompts the user for input. Prints the factored
    version of their input.
    """
    inp = prompt_single()
    if inp is not None:
        try:
            print(algebra.factor_expression(inp))
        except:
            print("Could not factor expression.")



def main():
    inp = print_menu()
    goto_function(inp)


if __name__ == "__main__":
    main()